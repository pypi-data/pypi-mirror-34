# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:40:07 2017
Copyright (C) 2018
@author: Derek Pisner
"""
import numpy as np


def wb_functional_connectometry(func_file, ID, atlas_select, network, node_size, mask, thr, parlistfile, conn_model,
                                dens_thresh, conf, plot_switch, parc, ref_txt, procmem, dir_path, multi_thr,
                                multi_atlas, max_thr, min_thr, step_thr, k, clust_mask, k_min, k_max, k_step,
                                k_clustering, user_atlas_list, clust_mask_list, node_size_list, conn_model_list,
                                min_span_tree, use_AAL_naming, smooth, smooth_list):
    import os
    from nipype.pipeline import engine as pe
    from nipype.interfaces import utility as niu
    from pynets import nodemaker, utils, graphestimation, plotting, thresholding
    import_list = ["import sys", "import os", "import numpy as np", "import networkx as nx", "import nibabel as nib"]
    wb_functional_connectometry_wf = pe.Workflow(name='wb_functional_connectometry_' + str(ID))
    base_dirname = "%s%s%s%s" % ('wb_functional_connectometry_', str(ID), '/Meta_wf_imp_est_', str(ID))
    wb_functional_connectometry_wf.base_directory = os.path.dirname(func_file) + base_dirname

    # Create input/output nodes
    #1) Add variable to IdentityInterface if user-set
    inputnode = pe.Node(niu.IdentityInterface(fields=['func_file', 'ID',
                                                      'atlas_select', 'network',
                                                      'node_size', 'mask', 'thr',
                                                      'parlistfile', 'multi_nets',
                                                      'conn_model', 'dens_thresh',
                                                      'conf', 'plot_switch', 'parc', 'ref_txt',
                                                      'procmem', 'dir_path', 'k',
                                                      'clust_mask', 'k_min', 'k_max',
                                                      'k_step', 'k_clustering', 'user_atlas_list',
                                                      'min_span_tree', 'use_AAL_naming', 'smooth']), name='inputnode')

    #2) Add variable to input nodes if user-set (e.g. inputnode.inputs.WHATEVER)
    inputnode.inputs.func_file = func_file
    inputnode.inputs.ID = ID
    inputnode.inputs.atlas_select = atlas_select
    inputnode.inputs.network = network
    inputnode.inputs.node_size = node_size
    inputnode.inputs.mask = mask
    inputnode.inputs.thr = thr
    inputnode.inputs.parlistfile = parlistfile
    inputnode.inputs.conn_model = conn_model
    inputnode.inputs.dens_thresh = dens_thresh
    inputnode.inputs.conf = conf
    inputnode.inputs.plot_switch = plot_switch
    inputnode.inputs.parc = parc
    inputnode.inputs.ref_txt = ref_txt
    inputnode.inputs.procmem = procmem
    inputnode.inputs.dir_path = dir_path
    inputnode.inputs.k = k
    inputnode.inputs.clust_mask = clust_mask
    inputnode.inputs.k_min = k_min
    inputnode.inputs.k_max = k_max
    inputnode.inputs.k_step = k_step
    inputnode.inputs.k_clustering = k_clustering
    inputnode.inputs.user_atlas_list = user_atlas_list
    inputnode.inputs.multi_thr = multi_thr
    inputnode.inputs.multi_atlas = multi_atlas
    inputnode.inputs.max_thr = max_thr
    inputnode.inputs.min_thr = min_thr
    inputnode.inputs.step_thr = step_thr
    inputnode.inputs.clust_mask_list = clust_mask_list
    inputnode.inputs.multi_nets = None
    inputnode.inputs.conn_model_list = conn_model_list
    inputnode.inputs.min_span_tree = min_span_tree
    inputnode.inputs.use_AAL_naming = use_AAL_naming
    inputnode.inputs.smooth = smooth

    #3) Add variable to function nodes
    # Create function nodes
    clustering_node = pe.Node(niu.Function(input_names=['func_file', 'clust_mask', 'ID', 'k'],
                                           output_names=['parlistfile', 'atlas_select', 'dir_path'],
                                           function=utils.individual_tcorr_clustering,
                                           imports=import_list), name="clustering_node")
    if k_clustering == 2 or k_clustering == 3 or k_clustering == 4:
        clustering_node._mem_gb = 10
        clustering_node.n_procs = 1
    WB_fetch_nodes_and_labels_node = pe.Node(niu.Function(input_names=['atlas_select', 'parlistfile', 'ref_txt',
                                                                       'parc', 'func_file', 'mask', 'use_AAL_naming'],
                                                          output_names=['label_names', 'coords', 'atlas_select',
                                                                        'networks_list', 'parcel_list', 'par_max',
                                                                        'parlistfile', 'dir_path'],
                                                          function=nodemaker.WB_fetch_nodes_and_labels,
                                                          imports=import_list), name="WB_fetch_nodes_and_labels_node")

    # Node generation
    if mask is not None:
        node_gen_node = pe.Node(niu.Function(input_names=['mask', 'coords', 'parcel_list', 'label_names', 'dir_path',
                                                          'ID', 'parc'],
                                             output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
                                             function=nodemaker.node_gen_masking, imports=import_list),
                                name="node_gen_masking_node")
    else:
        node_gen_node = pe.Node(niu.Function(input_names=['coords', 'parcel_list', 'label_names', 'dir_path',
                                                          'ID', 'parc'],
                                             output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
                                             function=nodemaker.node_gen, imports=import_list), name="node_gen_node")
    node_gen_node.interface.mem_gb = 2
    node_gen_node.interface.n_procs = 1
    node_gen_node._mem_gb = 2
    node_gen_node.n_procs = 1
    # Extract time-series from nodes
    extract_ts_iterables = []
    if parc is True:
        save_nifti_parcels_node = pe.Node(niu.Function(input_names=['ID', 'dir_path', 'mask', 'network',
                                                                    'net_parcels_map_nifti'],
                                                       function=utils.save_nifti_parcels_map, imports=import_list),
                                          name="save_nifti_parcels_node")
        # extract time series from whole brain parcellaions:
        extract_ts_wb_node = pe.Node(niu.Function(input_names=['net_parcels_map_nifti', 'conf', 'func_file', 'coords',
                                                               'mask', 'dir_path', 'ID', 'network', 'smooth'],
                                                  output_names=['ts_within_nodes', 'node_size', 'smooth'],
                                                  function=graphestimation.extract_ts_parc, imports=import_list),
                                     name="extract_ts_wb_parc_node")
    else:
        # Extract within-spheres time-series from funct file
        extract_ts_wb_node = pe.Node(niu.Function(input_names=['node_size', 'conf', 'func_file', 'coords', 'dir_path',
                                                               'ID', 'mask', 'network', 'smooth'],
                                                  output_names=['ts_within_nodes', 'node_size', 'smooth'],
                                                  function=graphestimation.extract_ts_coords, imports=import_list),
                                     name="extract_ts_wb_coords_node")
        if node_size_list:
            extract_ts_iterables.append(("node_size", node_size_list))
            extract_ts_wb_node.iterables = extract_ts_iterables
    if smooth_list:
        extract_ts_iterables.append(("smooth", smooth_list))
        extract_ts_wb_node.iterables = extract_ts_iterables
    extract_ts_wb_node.interface.mem_gb = 6
    extract_ts_wb_node.interface.n_procs = 1
    extract_ts_wb_node._mem_gb = 6
    extract_ts_wb_node.n_procs = 1

    get_conn_matrix_node = pe.Node(niu.Function(input_names=['time_series', 'conn_model'],
                                                output_names=['conn_matrix', 'conn_model'],
                                                function=graphestimation.get_conn_matrix, imports=import_list),
                                   name="get_conn_matrix_node")

    get_conn_matrix_node.interface.mem_gb = 4
    get_conn_matrix_node.interface.n_procs = 1
    get_conn_matrix_node._mem_gb = 4
    get_conn_matrix_node.n_procs = 1

    thresh_func_node = pe.Node(niu.Function(input_names=['dens_thresh', 'thr', 'conn_matrix', 'conn_model',
                                                         'network', 'ID', 'dir_path', 'mask', 'node_size',
                                                         'min_span_tree', 'smooth'],
                                            output_names=['conn_matrix_thr', 'edge_threshold', 'est_path', 'thr',
                                                          'node_size', 'network', 'conn_model', 'mask', 'smooth'],
                                            function=thresholding.thresh_func, imports=import_list),
                               name="thresh_func_node")

    # Plotting
    if plot_switch is True:
        plot_all_node = pe.Node(niu.Function(input_names=['conn_matrix', 'conn_model', 'atlas_select', 'dir_path',
                                                          'ID', 'network', 'label_names', 'mask', 'coords', 'thr',
                                                          'node_size', 'edge_threshold', 'smooth'],
                                             output_names='None',
                                             function=plotting.plot_all, imports=import_list),
                                name="plot_all_node")

    outputnode = pe.JoinNode(interface=niu.IdentityInterface(fields=['est_path', 'thr', 'network', 'conn_model',
                                                                     'node_size', 'smooth']), name='outputnode',
                             joinfield=['est_path', 'thr', 'network', 'conn_model', 'node_size', 'smooth'],
                             joinsource='thresh_func_node')

    thresh_func_node_iterables = []
    get_conn_matrix_node_iterables = []
    if multi_thr is True:
        iter_thresh = sorted(list(set([str(i) for i in np.round(np.arange(float(min_thr),
                                                                          float(max_thr), float(step_thr)),
                                                                decimals=2).tolist()] + [str(float(max_thr))])))
        thresh_func_node_iterables.append(("thr", iter_thresh))
        if conn_model_list:
            get_conn_matrix_node_iterables.append(("conn_model", conn_model_list))
        else:
            get_conn_matrix_node_iterables.append(("conn_model", [conn_model]))
    else:
        if conn_model_list:
            get_conn_matrix_node_iterables.append(("conn_model", conn_model_list))
            thresh_func_node_iterables.append(("thr", [thr]))
        else:
            get_conn_matrix_node_iterables.append(("conn_model", [conn_model]))
            thresh_func_node_iterables.append(("thr", [thr]))
    get_conn_matrix_node.iterables = get_conn_matrix_node_iterables
    thresh_func_node.iterables = thresh_func_node_iterables

    if (multi_atlas is not None and user_atlas_list is None and parlistfile is None) or (multi_atlas is None and atlas_select is None and user_atlas_list is not None):
        flexi_atlas = False
        if multi_atlas:
            WB_fetch_nodes_and_labels_node_iterables = []
            WB_fetch_nodes_and_labels_node_iterables.append(("atlas_select", multi_atlas))
            WB_fetch_nodes_and_labels_node.iterables = WB_fetch_nodes_and_labels_node_iterables
        elif user_atlas_list:
            WB_fetch_nodes_and_labels_node_iterables = []
            WB_fetch_nodes_and_labels_node_iterables.append(("parlistfile", user_atlas_list))
            WB_fetch_nodes_and_labels_node.iterables = WB_fetch_nodes_and_labels_node_iterables
    elif ((atlas_select is not None and parlistfile is None) or (atlas_select is None and parlistfile is not None)) and (multi_atlas is None and user_atlas_list is None):
        flexi_atlas = False
        pass
    else:
        flexi_atlas = True
        flexi_atlas_source = pe.Node(niu.IdentityInterface(fields=['atlas_select', 'parlistfile']),
                                     name='flexi_atlas_source')
        if multi_atlas is not None and user_atlas_list is not None:
            flexi_atlas_source_iterables = [("atlas_select", len(user_atlas_list) * [None] + multi_atlas),
                                            ("parlistfile", user_atlas_list + len(multi_atlas) * [None])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif multi_atlas is not None and parlistfile is not None and user_atlas_list is None:
            flexi_atlas_source_iterables = [("atlas_select", multi_atlas + [None]),
                                            ("parlistfile", len(multi_atlas) * [None] + [parlistfile])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif atlas_select is not None and user_atlas_list is not None and multi_atlas is None:
            flexi_atlas_source_iterables = [("atlas_select", len(user_atlas_list) * [None] + [atlas_select]),
                                            ("parlistfile", user_atlas_list + [None])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif atlas_select is not None and parlistfile is not None and user_atlas_list is None and multi_atlas is None:
            flexi_atlas_source_iterables = [("atlas_select", [atlas_select, None]),
                                            ("parlistfile", [None, parlistfile])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True

    if k_clustering == 2:
        k_cluster_iterables = []
        k_list = np.round(np.arange(int(k_min), int(k_max), int(k_step)), decimals=0).tolist() + [int(k_max)]
        k_cluster_iterables.append(("k", k_list))
        clustering_node.iterables = k_cluster_iterables
    elif k_clustering == 3:
        k_cluster_iterables = []
        k_cluster_iterables.append(("clust_mask", clust_mask_list))
        clustering_node.iterables = k_cluster_iterables
    elif k_clustering == 4:
        k_cluster_iterables = []
        k_list = np.round(np.arange(int(k_min), int(k_max), int(k_step)), decimals=0).tolist() + [int(k_max)]
        k_cluster_iterables.append(("k", k_list))
        k_cluster_iterables.append(("clust_mask", clust_mask_list))
        clustering_node.iterables = k_cluster_iterables

    # Connect nodes of workflow
    wb_functional_connectometry_wf.connect([
        (inputnode, WB_fetch_nodes_and_labels_node, [('func_file', 'func_file'),
                                                     ('atlas_select', 'atlas_select'),
                                                     ('parlistfile', 'parlistfile'),
                                                     ('parc', 'parc'), ('ref_txt', 'ref_txt'),
                                                     ('use_AAL_naming', 'use_AAL_naming')]),
        (inputnode, node_gen_node, [('ID', 'ID'),
                                    ('mask', 'mask'),
                                    ('parc', 'parc')]),
        (WB_fetch_nodes_and_labels_node, node_gen_node, [('coords', 'coords'), ('label_names', 'label_names'),
                                                         ('dir_path', 'dir_path'), ('parcel_list', 'parcel_list'),
                                                         ('par_max', 'par_max'), ('networks_list', 'networks_list')]),
        (inputnode, extract_ts_wb_node, [('conf', 'conf'), ('func_file', 'func_file'), ('node_size', 'node_size'),
                                         ('mask', 'mask'), ('ID', 'ID'), ('network', 'network'), ('thr', 'thr'),
                                         ('smooth', 'smooth')]),
        (WB_fetch_nodes_and_labels_node, extract_ts_wb_node, [('dir_path', 'dir_path')]),
        (node_gen_node, extract_ts_wb_node, [('net_parcels_map_nifti', 'net_parcels_map_nifti'),
                                             ('coords', 'coords')]),
        (inputnode, thresh_func_node, [('dens_thresh', 'dens_thresh'),
                                       ('thr', 'thr'),
                                       ('ID', 'ID'),
                                       ('mask', 'mask'),
                                       ('network', 'network'),
                                       ('min_span_tree', 'min_span_tree')]),
        (WB_fetch_nodes_and_labels_node, thresh_func_node, [('dir_path', 'dir_path')]),
        (extract_ts_wb_node, get_conn_matrix_node, [('ts_within_nodes', 'time_series')]),
        (extract_ts_wb_node, thresh_func_node, [('node_size', 'node_size'), ('smooth', 'smooth')]),
        (get_conn_matrix_node, thresh_func_node, [('conn_matrix', 'conn_matrix'), ('conn_model', 'conn_model')]),
        (thresh_func_node, outputnode, [('est_path', 'est_path'), ('thr', 'thr'), ('node_size', 'node_size'),
                                        ('network', 'network'), ('conn_model', 'conn_model'), ('smooth', 'smooth')])
        ])

    if plot_switch is True:
        wb_functional_connectometry_wf.connect([(inputnode, plot_all_node, [('ID', 'ID'),
                                                                            ('mask', 'mask'),
                                                                            ('network', 'network')]),
                                                (extract_ts_wb_node, plot_all_node, [('node_size', 'node_size'),
                                                                                     ('smooth', 'smooth')]),
                                                (WB_fetch_nodes_and_labels_node, plot_all_node,
                                                 [('dir_path', 'dir_path'),
                                                  ('atlas_select', 'atlas_select')]),
                                                (node_gen_node, plot_all_node, [('label_names', 'label_names'),
                                                                                ('coords', 'coords')]),
                                                (thresh_func_node, plot_all_node,
                                                 [('conn_matrix_thr', 'conn_matrix'),
                                                  ('edge_threshold', 'edge_threshold'),
                                                  ('thr', 'thr'), ('conn_model', 'conn_model')]),
                                                ])
    if k_clustering == 4 or k_clustering == 3 or k_clustering == 2 or k_clustering == 1:
        wb_functional_connectometry_wf.add_nodes([clustering_node])
        if plot_switch is True:
            wb_functional_connectometry_wf.disconnect([(inputnode, WB_fetch_nodes_and_labels_node,
                                                        [('parlistfile', 'parlistfile'),
                                                         ('atlas_select', 'atlas_select')]),
                                                       (WB_fetch_nodes_and_labels_node, plot_all_node,
                                                        [('atlas_select', 'atlas_select')])
                                                       ])
            wb_functional_connectometry_wf.connect([(inputnode, clustering_node, [('ID', 'ID'),
                                                                                  ('func_file', 'func_file'),
                                                                                  ('clust_mask', 'clust_mask'),
                                                                                  ('k', 'k')]),
                                                    (clustering_node, WB_fetch_nodes_and_labels_node,
                                                     [('parlistfile', 'parlistfile'),
                                                      ('atlas_select', 'atlas_select')]),
                                                    (clustering_node, plot_all_node,
                                                     [('atlas_select', 'atlas_select')]),
                                                    ])
        else:
            wb_functional_connectometry_wf.disconnect([(inputnode, WB_fetch_nodes_and_labels_node,
                                                        [('parlistfile', 'parlistfile'),
                                                         ('atlas_select', 'atlas_select')])
                                                       ])
            wb_functional_connectometry_wf.connect([(inputnode, clustering_node, [('ID', 'ID'),
                                                                                  ('func_file', 'func_file'),
                                                                                  ('clust_mask', 'clust_mask'),
                                                                                  ('k', 'k')]),
                                                    (clustering_node, WB_fetch_nodes_and_labels_node,
                                                     [('parlistfile', 'parlistfile'),
                                                      ('atlas_select', 'atlas_select')])
                                                    ])
    if parc is True:
        wb_functional_connectometry_wf.add_nodes([save_nifti_parcels_node])
        wb_functional_connectometry_wf.connect([(inputnode, save_nifti_parcels_node, [('ID', 'ID'), ('mask', 'mask')]),
                                                (inputnode, save_nifti_parcels_node, [('network', 'network')]),
                                                (WB_fetch_nodes_and_labels_node, save_nifti_parcels_node,
                                                 [('dir_path', 'dir_path')]),
                                                (node_gen_node, save_nifti_parcels_node,
                                                 [('net_parcels_map_nifti', 'net_parcels_map_nifti')])
                                                ])
    else:
        wb_functional_connectometry_wf.disconnect([(node_gen_node, extract_ts_wb_node,
                                                    [('net_parcels_map_nifti', 'net_parcels_map_nifti'),
                                                     ('coords', 'coords')])
                                                   ])
        wb_functional_connectometry_wf.connect([(node_gen_node, extract_ts_wb_node, [('coords', 'coords')])
                                                ])
    if flexi_atlas is True:
        if k_clustering == 4 or k_clustering == 3 or k_clustering == 2 or k_clustering == 1:
            wb_functional_connectometry_wf.disconnect([(inputnode, clustering_node,
                                                        [('parlistfile', 'parlistfile')])
                                                       ])
            wb_functional_connectometry_wf.connect([(flexi_atlas_source, clustering_node,
                                                     [('parlistfile', 'parlistfile')])
                                                    ])
        else:
            wb_functional_connectometry_wf.disconnect([(inputnode, WB_fetch_nodes_and_labels_node,
                                                        [('atlas_select', 'atlas_select'),
                                                         ('parlistfile', 'parlistfile')])
                                                       ])
            wb_functional_connectometry_wf.connect([(flexi_atlas_source, WB_fetch_nodes_and_labels_node,
                                                     [('atlas_select', 'atlas_select'), ('parlistfile', 'parlistfile')])
                                                    ])
    wb_functional_connectometry_wf.config['execution']['crashdump_dir'] = wb_functional_connectometry_wf.base_directory
    wb_functional_connectometry_wf.config['execution']['crashfile_format'] = 'txt'
    wb_functional_connectometry_wf.config['logging']['log_directory'] = wb_functional_connectometry_wf.base_directory
    wb_functional_connectometry_wf.config['logging']['workflow_level'] = 'DEBUG'
    wb_functional_connectometry_wf.config['logging']['utils_level'] = 'DEBUG'
    wb_functional_connectometry_wf.config['logging']['interface_level'] = 'DEBUG'
    wb_functional_connectometry_wf.config['execution']['display_variable'] = ':0'

    return wb_functional_connectometry_wf


def rsn_functional_connectometry(func_file, ID, atlas_select, network, node_size, mask, thr, parlistfile, multi_nets,
                                 conn_model, dens_thresh, conf, plot_switch, parc, ref_txt, procmem, dir_path,
                                 multi_thr, multi_atlas, max_thr, min_thr, step_thr, k, clust_mask, k_min, k_max,
                                 k_step, k_clustering, user_atlas_list, clust_mask_list, node_size_list, conn_model_list,
                                 min_span_tree, use_AAL_naming, smooth, smooth_list):
    import os
    from nipype.pipeline import engine as pe
    from nipype.interfaces import utility as niu
    from pynets import nodemaker, utils, graphestimation, plotting, thresholding
    import_list = ["import sys", "import os", "import numpy as np", "import networkx as nx", "import nibabel as nib"]

    rsn_functional_connectometry_wf = pe.Workflow(name='rsn_functional_connectometry_' + str(ID))
    base_dirname = "%s%s%s%s" % ('rsn_functional_connectometry_', str(ID), '/Meta_wf_imp_est_', str(ID))
    rsn_functional_connectometry_wf.base_directory = os.path.dirname(func_file) + base_dirname

    # Create input/output nodes
    #1) Add variable to IdentityInterface if user-set
    inputnode = pe.Node(niu.IdentityInterface(fields=['func_file', 'ID',
                                                      'atlas_select', 'network',
                                                      'node_size', 'mask', 'thr',
                                                      'parlistfile', 'multi_nets',
                                                      'conn_model', 'dens_thresh',
                                                      'conf', 'plot_switch', 'parc', 'ref_txt',
                                                      'procmem', 'dir_path', 'k',
                                                      'clust_mask', 'k_min', 'k_max',
                                                      'k_step', 'k_clustering', 'user_atlas_list',
                                                      'min_span_tree', 'use_AAL_naming', 'smooth']), name='inputnode')

    #2)Add variable to input nodes if user-set (e.g. inputnode.inputs.WHATEVER)
    inputnode.inputs.func_file = func_file
    inputnode.inputs.ID = ID
    inputnode.inputs.atlas_select = atlas_select
    inputnode.inputs.network = network
    inputnode.inputs.node_size = node_size
    inputnode.inputs.mask = mask
    inputnode.inputs.thr = thr
    inputnode.inputs.parlistfile = parlistfile
    inputnode.inputs.conn_model = conn_model
    inputnode.inputs.dens_thresh = dens_thresh
    inputnode.inputs.conf = conf
    inputnode.inputs.plot_switch = plot_switch
    inputnode.inputs.parc = parc
    inputnode.inputs.ref_txt = ref_txt
    inputnode.inputs.procmem = procmem
    inputnode.inputs.dir_path = dir_path
    inputnode.inputs.k = k
    inputnode.inputs.clust_mask = clust_mask
    inputnode.inputs.k_min = k_min
    inputnode.inputs.k_max = k_max
    inputnode.inputs.k_step = k_step
    inputnode.inputs.k_clustering = k_clustering
    inputnode.inputs.user_atlas_list = user_atlas_list
    inputnode.inputs.multi_thr = multi_thr
    inputnode.inputs.multi_atlas = multi_atlas
    inputnode.inputs.max_thr = max_thr
    inputnode.inputs.min_thr = min_thr
    inputnode.inputs.step_thr = step_thr
    inputnode.inputs.clust_mask_list = clust_mask_list
    inputnode.inputs.multi_nets = multi_nets
    inputnode.inputs.conn_model_list = conn_model_list
    inputnode.inputs.min_span_tree = min_span_tree
    inputnode.inputs.use_AAL_naming = use_AAL_naming
    inputnode.inputs.smooth = smooth

    #3) Add variable to function nodes
    # Create function nodes
    clustering_node = pe.Node(niu.Function(input_names=['func_file', 'clust_mask', 'ID', 'k'],
                                           output_names=['parlistfile', 'atlas_select', 'dir_path'],
                                           function=utils.individual_tcorr_clustering,
                                           imports=import_list), name="clustering_node")
    if k_clustering == 2 or k_clustering == 3 or k_clustering == 4:
        clustering_node._mem_gb = 8
        clustering_node.n_procs = 1
    RSN_fetch_nodes_and_labels_node = pe.Node(niu.Function(input_names=['atlas_select', 'parlistfile', 'ref_txt',
                                                                        'parc', 'func_file', 'use_AAL_naming'],
                                                           output_names=['label_names', 'coords', 'atlas_select',
                                                                         'networks_list', 'parcel_list', 'par_max',
                                                                         'parlistfile', 'dir_path'],
                                                           function=nodemaker.RSN_fetch_nodes_and_labels,
                                                           imports=import_list),
                                              name="RSN_fetch_nodes_and_labels_node")
    get_node_membership_node = pe.Node(niu.Function(input_names=['network', 'func_file', 'coords', 'label_names',
                                                                 'parc', 'parcel_list'],
                                                    output_names=['net_coords', 'net_parcel_list', 'net_label_names',
                                                                  'network'],
                                                    function=nodemaker.get_node_membership, imports=import_list),
                                       name="get_node_membership_node")
    # Node generation
    if mask is not None:
        node_gen_node = pe.Node(niu.Function(input_names=['mask', 'coords', 'parcel_list', 'label_names', 'dir_path',
                                                          'ID', 'parc'],
                                             output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
                                             function=nodemaker.node_gen_masking, imports=import_list),
                                name="node_gen_masking_node")
    else:
        node_gen_node = pe.Node(niu.Function(input_names=['coords', 'parcel_list', 'label_names', 'dir_path', 'ID',
                                                          'parc'],
                                             output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
                                             function=nodemaker.node_gen, imports=import_list), name="node_gen_node")
    node_gen_node.interface.mem_gb = 2
    node_gen_node.interface.n_procs = 1
    node_gen_node._mem_gb = 2
    node_gen_node.n_procs = 1
    save_coords_and_labels_node = pe.Node(niu.Function(input_names=['coords', 'label_names', 'dir_path', 'network'],
                                                       function=utils.save_RSN_coords_and_labels_to_pickle,
                                                       imports=import_list), name="save_coords_and_labels_node")
    # Extract time-series from nodes
    extract_ts_iterables = []
    if parc is True:
        save_nifti_parcels_node = pe.Node(niu.Function(input_names=['ID', 'dir_path', 'mask', 'network',
                                                                    'net_parcels_map_nifti'],
                                                       function=utils.save_nifti_parcels_map, imports=import_list),
                                          name="save_nifti_parcels_node")
        # Extract time series from whole brain parcellaions:
        extract_ts_rsn_node = pe.Node(niu.Function(input_names=['net_parcels_map_nifti', 'conf', 'func_file', 'coords',
                                                                'mask', 'dir_path', 'ID', 'network', 'smooth'],
                                                   output_names=['ts_within_nodes', 'node_size', 'smooth'],
                                                   function=graphestimation.extract_ts_parc, imports=import_list),
                                      name="extract_ts_rsn_parc_node")
    else:
        # Extract within-spheres time-series from funct file
        extract_ts_rsn_node = pe.Node(niu.Function(input_names=['node_size', 'conf', 'func_file', 'coords', 'dir_path',
                                                                'ID', 'mask', 'network', 'smooth'],
                                                   output_names=['ts_within_nodes', 'node_size', 'smooth'],
                                                   function=graphestimation.extract_ts_coords, imports=import_list),
                                      name="extract_ts_rsn_coords_node")
        if node_size_list:
            extract_ts_iterables.append(("node_size", node_size_list))
            extract_ts_rsn_node.iterables = extract_ts_iterables
    if smooth_list:
        extract_ts_iterables.append(("smooth", smooth_list))
        extract_ts_rsn_node.iterables = extract_ts_iterables
    extract_ts_rsn_node.interface.mem_gb = 6
    extract_ts_rsn_node.interface.n_procs = 1
    extract_ts_rsn_node._mem_gb = 6
    extract_ts_rsn_node.n_procs = 1

    get_conn_matrix_node = pe.Node(niu.Function(input_names=['time_series', 'conn_model'],
                                                output_names=['conn_matrix', 'conn_model'],
                                                function=graphestimation.get_conn_matrix, imports=import_list),
                                   name="get_conn_matrix_node")
    get_conn_matrix_node.interface.mem_gb = 4
    get_conn_matrix_node.interface.n_procs = 1
    get_conn_matrix_node._mem_gb = 4
    get_conn_matrix_node.n_procs = 1

    thresh_func_node = pe.Node(niu.Function(input_names=['dens_thresh', 'thr', 'conn_matrix', 'conn_model',
                                                         'network', 'ID', 'dir_path', 'mask', 'node_size',
                                                         'min_span_tree', 'smooth'],
                                            output_names=['conn_matrix_thr', 'edge_threshold', 'est_path', 'thr',
                                                          'node_size', 'network', 'conn_model', 'mask', 'smooth'],
                                            function=thresholding.thresh_func, imports=import_list),
                               name="thresh_func_node")

    # Plotting
    if plot_switch is True:
        plot_all_node = pe.Node(niu.Function(input_names=['conn_matrix', 'conn_model', 'atlas_select', 'dir_path',
                                                          'ID', 'network', 'label_names', 'mask', 'coords', 'thr',
                                                          'node_size', 'edge_threshold', 'smooth'], output_names='None',
                                             function=plotting.plot_all, imports=import_list), name="plot_all_node")
    outputnode = pe.JoinNode(interface=niu.IdentityInterface(fields=['est_path', 'thr', 'node_size', 'network',
                                                                     'conn_model', 'smooth']),
                             name='outputnode',
                             joinfield=['est_path', 'thr', 'node_size', 'network', 'conn_model', 'smooth'],
                             joinsource='thresh_func_node')

    thresh_func_node_iterables = []
    get_conn_matrix_node_iterables = []
    if multi_thr is True:
        iter_thresh = sorted(list(set([str(i) for i in np.round(np.arange(float(min_thr),
                                                                          float(max_thr), float(step_thr)),
                                                                decimals=2).tolist()] + [str(float(max_thr))])))
        thresh_func_node_iterables.append(("thr", iter_thresh))
        if conn_model_list:
            get_conn_matrix_node_iterables.append(("conn_model", conn_model_list))
        else:
            get_conn_matrix_node_iterables.append(("conn_model", [conn_model]))
    else:
        if conn_model_list:
            get_conn_matrix_node_iterables.append(("conn_model", conn_model_list))
            thresh_func_node_iterables.append(("thr", [thr]))
        else:
            get_conn_matrix_node_iterables.append(("conn_model", [conn_model]))
            thresh_func_node_iterables.append(("thr", [thr]))
    get_conn_matrix_node.iterables = get_conn_matrix_node_iterables
    thresh_func_node.iterables = thresh_func_node_iterables

    if (multi_atlas is not None and user_atlas_list is None and parlistfile is None) or (multi_atlas is None and atlas_select is None and user_atlas_list is not None):
        flexi_atlas = False
        if multi_atlas is not None and user_atlas_list is None:
            RSN_fetch_nodes_and_labels_node_iterables = []
            RSN_fetch_nodes_and_labels_node_iterables.append(("atlas_select", multi_atlas))
            RSN_fetch_nodes_and_labels_node.iterables = RSN_fetch_nodes_and_labels_node_iterables
        elif multi_atlas is None and user_atlas_list is not None:
            RSN_fetch_nodes_and_labels_node_iterables = []
            RSN_fetch_nodes_and_labels_node_iterables.append(("parlistfile", user_atlas_list))
            RSN_fetch_nodes_and_labels_node.iterables = RSN_fetch_nodes_and_labels_node_iterables
    elif ((atlas_select is not None and parlistfile is None) or (atlas_select is None and parlistfile is not None)) and (multi_atlas is None and user_atlas_list is None):
        flexi_atlas = False
        pass
    else:
        flexi_atlas = True
        flexi_atlas_source = pe.Node(niu.IdentityInterface(fields=['atlas_select', 'parlistfile']),
                                     name='flexi_atlas_source')
        if multi_atlas is not None and user_atlas_list is not None:
            flexi_atlas_source_iterables = [("atlas_select", len(user_atlas_list) * [None] + multi_atlas),
                                            ("parlistfile", user_atlas_list + len(multi_atlas) * [None])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif multi_atlas is not None and parlistfile is not None and user_atlas_list is None:
            flexi_atlas_source_iterables = [("atlas_select", multi_atlas + [None]),
                                            ("parlistfile", len(multi_atlas) * [None] + [parlistfile])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif atlas_select is not None and user_atlas_list is not None and multi_atlas is None:
            flexi_atlas_source_iterables = [("atlas_select", len(user_atlas_list) * [None] + [atlas_select]),
                                            ("parlistfile", user_atlas_list + [None])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif atlas_select is not None and parlistfile is not None and user_atlas_list is None and multi_atlas is None:
            flexi_atlas_source_iterables = [("atlas_select", [atlas_select, None]),
                                            ("parlistfile", [None, parlistfile])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True

    if multi_nets is not None:
        get_node_membership_node_iterables = []
        network_iterables = ("network", multi_nets)
        get_node_membership_node_iterables.append(network_iterables)
        get_node_membership_node.iterables = get_node_membership_node_iterables
    if k_clustering == 2:
        k_cluster_iterables = []
        k_list = np.round(np.arange(int(k_min), int(k_max), int(k_step)), decimals=0).tolist() + [int(k_max)]
        k_cluster_iterables.append(("k", k_list))
        clustering_node.iterables = k_cluster_iterables
    elif k_clustering == 3:
        k_cluster_iterables = []
        k_cluster_iterables.append(("clust_mask", clust_mask_list))
        clustering_node.iterables = k_cluster_iterables
    elif k_clustering == 4:
        k_cluster_iterables = []
        k_list = np.round(np.arange(int(k_min), int(k_max), int(k_step)), decimals=0).tolist() + [int(k_max)]
        k_cluster_iterables.append(("k", k_list))
        k_cluster_iterables.append(("clust_mask", clust_mask_list))
        clustering_node.iterables = k_cluster_iterables

    # Connect nodes of workflow
    rsn_functional_connectometry_wf.connect([
        (inputnode, RSN_fetch_nodes_and_labels_node, [('atlas_select', 'atlas_select'),
                                                      ('parlistfile', 'parlistfile'),
                                                      ('parc', 'parc'),
                                                      ('ref_txt', 'ref_txt'),
                                                      ('func_file', 'func_file'),
                                                      ('use_AAL_naming', 'use_AAL_naming')]),
        (inputnode, get_node_membership_node, [('network', 'network'),
                                               ('func_file', 'func_file'),
                                               ('parc', 'parc')]),
        (RSN_fetch_nodes_and_labels_node, get_node_membership_node, [('coords', 'coords'),
                                                                     ('label_names', 'label_names'),
                                                                     ('parcel_list', 'parcel_list'),
                                                                     ('par_max', 'par_max'),
                                                                     ('networks_list', 'networks_list')]),
        (inputnode, node_gen_node, [('ID', 'ID'),
                                    ('mask', 'mask'),
                                    ('parc', 'parc')]),
        (RSN_fetch_nodes_and_labels_node, node_gen_node, [('dir_path', 'dir_path')]),
        (get_node_membership_node, node_gen_node, [('net_coords', 'coords'),
                                                   ('net_label_names', 'label_names'),
                                                   ('net_parcel_list', 'parcel_list')]),
        (get_node_membership_node, save_coords_and_labels_node, [('net_coords', 'coords'),
                                                                 ('net_label_names', 'label_names'),
                                                                 ('network', 'network')]),
        (RSN_fetch_nodes_and_labels_node, save_coords_and_labels_node, [('dir_path', 'dir_path')]),
        (inputnode, extract_ts_rsn_node, [('conf', 'conf'), ('func_file', 'func_file'), ('node_size', 'node_size'),
                                          ('mask', 'mask'), ('ID', 'ID'), ('smooth', 'smooth')]),
        (get_node_membership_node, extract_ts_rsn_node, [('network', 'network')]),
        (RSN_fetch_nodes_and_labels_node, extract_ts_rsn_node, [('dir_path', 'dir_path')]),
        (node_gen_node, extract_ts_rsn_node, [('net_parcels_map_nifti', 'net_parcels_map_nifti'),
                                              ('coords', 'coords')]),
        (inputnode, thresh_func_node, [('dens_thresh', 'dens_thresh'),
                                       ('thr', 'thr'),
                                       ('ID', 'ID'),
                                       ('mask', 'mask'),
                                       ('min_span_tree', 'min_span_tree')]),
        (RSN_fetch_nodes_and_labels_node, thresh_func_node, [('dir_path', 'dir_path')]),
        (get_node_membership_node, thresh_func_node, [('network', 'network')]),
        (extract_ts_rsn_node, get_conn_matrix_node, [('ts_within_nodes', 'time_series')]),
        (extract_ts_rsn_node, thresh_func_node, [('node_size', 'node_size'), ('smooth', 'smooth')]),
        (get_conn_matrix_node, thresh_func_node, [('conn_matrix', 'conn_matrix'), ('conn_model', 'conn_model')]),
        (thresh_func_node, outputnode, [('est_path', 'est_path'), ('thr', 'thr'), ('node_size', 'node_size'),
                                        ('network', 'network'), ('conn_model', 'conn_model'), ('smooth', 'smooth')])
        ])
    if plot_switch is True:
        rsn_functional_connectometry_wf.connect([(inputnode, plot_all_node, [('ID', 'ID'),
                                                                             ('mask', 'mask'),
                                                                             ('network', 'network')]),
                                                (extract_ts_rsn_node, plot_all_node, [('node_size', 'node_size'),
                                                                                      ('smooth', 'smooth')]),
                                                (RSN_fetch_nodes_and_labels_node, plot_all_node,
                                                 [('dir_path', 'dir_path'),
                                                  ('atlas_select', 'atlas_select')]),
                                                (node_gen_node, plot_all_node, [('label_names', 'label_names'),
                                                                                ('coords', 'coords')]),
                                                (thresh_func_node, plot_all_node,
                                                 [('conn_matrix_thr', 'conn_matrix'),
                                                  ('edge_threshold', 'edge_threshold'),
                                                  ('thr', 'thr'), ('conn_model', 'conn_model')])
                                                 ])
    if k_clustering == 4 or k_clustering == 3 or k_clustering == 2 or k_clustering == 1:
        rsn_functional_connectometry_wf.add_nodes([clustering_node])
        if plot_switch is True:
            rsn_functional_connectometry_wf.disconnect([(inputnode, RSN_fetch_nodes_and_labels_node,
                                                         [('parlistfile', 'parlistfile'),
                                                          ('atlas_select', 'atlas_select')]),
                                                       (RSN_fetch_nodes_and_labels_node, plot_all_node,
                                                        [('atlas_select', 'atlas_select')])
                                                        ])
            rsn_functional_connectometry_wf.connect([(inputnode, clustering_node, [('ID', 'ID'),
                                                                                   ('func_file', 'func_file'),
                                                                                   ('clust_mask', 'clust_mask'),
                                                                                   ('k', 'k')]),
                                                    (clustering_node, RSN_fetch_nodes_and_labels_node,
                                                     [('parlistfile', 'parlistfile'),
                                                      ('atlas_select', 'atlas_select')]),
                                                    (clustering_node, plot_all_node,
                                                     [('atlas_select', 'atlas_select')])
                                                     ])
        else:
            rsn_functional_connectometry_wf.disconnect([(inputnode, RSN_fetch_nodes_and_labels_node,
                                                         [('parlistfile', 'parlistfile'),
                                                          ('atlas_select', 'atlas_select')])
                                                        ])
            rsn_functional_connectometry_wf.connect([(inputnode, clustering_node, [('ID', 'ID'),
                                                                                   ('func_file', 'func_file'),
                                                                                   ('clust_mask', 'clust_mask'),
                                                                                   ('k', 'k')]),
                                                    (clustering_node, RSN_fetch_nodes_and_labels_node,
                                                     [('parlistfile', 'parlistfile'),
                                                      ('atlas_select', 'atlas_select')])
                                                     ])
    if parc is True:
        rsn_functional_connectometry_wf.add_nodes([save_nifti_parcels_node])
        rsn_functional_connectometry_wf.connect([(inputnode, save_nifti_parcels_node, [('ID', 'ID'), ('mask', 'mask')]),
                                                (get_node_membership_node, save_nifti_parcels_node,
                                                 [('network', 'network')]),
                                                (RSN_fetch_nodes_and_labels_node, save_nifti_parcels_node,
                                                 [('dir_path', 'dir_path')]),
                                                (node_gen_node, save_nifti_parcels_node,
                                                 [('net_parcels_map_nifti', 'net_parcels_map_nifti')])
                                                 ])
    else:
        rsn_functional_connectometry_wf.disconnect([(node_gen_node, extract_ts_rsn_node,
                                                     [('net_parcels_map_nifti', 'net_parcels_map_nifti'),
                                                      ('coords', 'coords')])
                                                    ])
        rsn_functional_connectometry_wf.connect([(node_gen_node, extract_ts_rsn_node, [('coords', 'coords')])
                                                 ])
    if multi_nets is not None and plot_switch is True:
            rsn_functional_connectometry_wf.disconnect([(inputnode, plot_all_node, [('network', 'network')])
                                                        ])
            rsn_functional_connectometry_wf.connect([(get_node_membership_node, plot_all_node,
                                                     [('network', 'network')])
                                                     ])
    if flexi_atlas is True:
        if k_clustering == 4 or k_clustering == 3 or k_clustering == 2 or k_clustering == 1:
            rsn_functional_connectometry_wf.disconnect([(inputnode, clustering_node,
                                                         [('parlistfile', 'parlistfile')])
                                                        ])
            rsn_functional_connectometry_wf.connect([(flexi_atlas_source, clustering_node,
                                                     [('parlistfile', 'parlistfile')])
                                                     ])
        else:
            rsn_functional_connectometry_wf.disconnect([(inputnode, RSN_fetch_nodes_and_labels_node,
                                                         [('atlas_select', 'atlas_select'),
                                                          ('parlistfile', 'parlistfile')])
                                                        ])
            rsn_functional_connectometry_wf.connect([(flexi_atlas_source, RSN_fetch_nodes_and_labels_node,
                                                     [('atlas_select', 'atlas_select'), ('parlistfile', 'parlistfile')])
                                                     ])
    rsn_functional_connectometry_wf.config['execution']['crashdump_dir'] = rsn_functional_connectometry_wf.base_directory
    rsn_functional_connectometry_wf.config['execution']['crashfile_format'] = 'txt'
    rsn_functional_connectometry_wf.config['logging']['log_directory'] = rsn_functional_connectometry_wf.base_directory
    rsn_functional_connectometry_wf.config['logging']['workflow_level'] = 'DEBUG'
    rsn_functional_connectometry_wf.config['logging']['utils_level'] = 'DEBUG'
    rsn_functional_connectometry_wf.config['logging']['interface_level'] = 'DEBUG'
    rsn_functional_connectometry_wf.config['execution']['display_variable'] = ':0'

    return rsn_functional_connectometry_wf


def wb_structural_connectometry(ID, atlas_select, network, node_size, mask, parlistfile, plot_switch, parc, ref_txt,
                                procmem, dir_path, dwi_dir, anat_loc, thr, dens_thresh, conn_model,
                                user_atlas_list, multi_thr, multi_atlas, max_thr, min_thr, step_thr, node_size_list,
                                num_total_samples, conn_model_list, min_span_tree, use_AAL_naming):
    import os.path
    from nipype.pipeline import engine as pe
    from nipype.interfaces import utility as niu
    from pynets import nodemaker, diffconnectometry, plotting, thresholding

    nodif_brain_mask_path = "%s%s" % (dwi_dir, '/nodif_brain_mask.nii.gz')

    import_list = ["import sys", "import os", "import numpy as np", "import networkx as nx", "import nibabel as nib"]
    wb_structural_connectometry_wf = pe.Workflow(name='wb_structural_connectometry_' + str(ID))
    base_dirname = "%s%s%s%s" % ('wb_structural_connectometry_', str(ID), '/Meta_wf_imp_est_', str(ID))
    wb_structural_connectometry_wf.base_directory = dwi_dir + base_dirname

    # Create input/output nodes
    #1) Add variable to IdentityInterface if user-set
    inputnode = pe.Node(niu.IdentityInterface(fields=['ID', 'atlas_select', 'network', 'node_size', 'mask',
                                                      'parlistfile', 'plot_switch', 'parc', 'ref_txt', 'procmem',
                                                      'dir_path', 'dwi_dir', 'anat_loc', 'thr', 'dens_thresh',
                                                      'conn_model', 'user_atlas_list', 'multi_thr', 'multi_atlas',
                                                      'max_thr', 'min_thr', 'step_thr', 'num_total_samples',
                                                      'min_span_tree', 'use_AAL_naming']), name='inputnode')

    #2)Add variable to input nodes if user-set (e.g. inputnode.inputs.WHATEVER)
    inputnode.inputs.ID = ID
    inputnode.inputs.atlas_select = atlas_select
    inputnode.inputs.network = network
    inputnode.inputs.node_size = node_size
    inputnode.inputs.mask = mask
    inputnode.inputs.parlistfile = parlistfile
    inputnode.inputs.plot_switch = plot_switch
    inputnode.inputs.parc = parc
    inputnode.inputs.ref_txt = ref_txt
    inputnode.inputs.procmem = procmem
    inputnode.inputs.dir_path = dir_path
    inputnode.inputs.dwi_dir = dwi_dir
    inputnode.inputs.anat_loc = anat_loc
    inputnode.inputs.nodif_brain_mask_path = nodif_brain_mask_path
    inputnode.inputs.thr = thr
    inputnode.inputs.dens_thresh = dens_thresh
    inputnode.inputs.conn_model = conn_model
    inputnode.inputs.user_atlas_list = user_atlas_list
    inputnode.inputs.multi_thr = multi_thr
    inputnode.inputs.multi_atlas = multi_atlas
    inputnode.inputs.max_thr = max_thr
    inputnode.inputs.min_thr = min_thr
    inputnode.inputs.step_thr = step_thr
    inputnode.inputs.num_total_samples = num_total_samples
    inputnode.inputs.conn_model_list = conn_model_list
    inputnode.inputs.min_span_tree = min_span_tree
    inputnode.inputs.use_AAL_naming = use_AAL_naming

    #3) Add variable to function nodes
    # Create function nodes
    WB_fetch_nodes_and_labels_node = pe.Node(niu.Function(input_names=['atlas_select', 'parlistfile', 'ref_txt',
                                                                       'parc', 'func_file', 'mask', 'use_AAL_naming'],
                                                          output_names=['label_names', 'coords', 'atlas_select',
                                                                        'networks_list', 'parcel_list', 'par_max',
                                                                        'parlistfile', 'dir_path'],
                                                          function=nodemaker.WB_fetch_nodes_and_labels,
                                                          imports=import_list), name="WB_fetch_nodes_and_labels_node")
    # Node generation
    # if mask is not None:
    #     node_gen_node = pe.Node(niu.Function(input_names=['mask', 'coords', 'parcel_list', 'label_names', 'dir_path', 'ID', 'parc'],
    #                                                  output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
    #                                                  function=nodemaker.node_gen_masking, imports=import_list), name="node_gen_masking_node")
    # else:
    #     node_gen_node = pe.Node(niu.Function(input_names=['coords', 'parcel_list', 'label_names', 'dir_path', 'ID', 'parc'],
    #                                                  output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
    #                                                  function=nodemaker.node_gen, imports=import_list), name="node_gen_node")

    node_gen_node = pe.Node(niu.Function(input_names=['coords', 'parcel_list', 'label_names', 'dir_path', 'ID', 'parc'],
                                         output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
                                         function=nodemaker.node_gen, imports=import_list), name="node_gen_node")
    create_mni2diff_transforms_node = pe.Node(niu.Function(input_names=['dwi_dir'], output_names=['out_aff'],
                                                           function=diffconnectometry.create_mni2diff_transforms,
                                                           imports=import_list), name="create_mni2diff_transforms_node")
    CSF_file = "%s%s" % (anat_loc, '/CSF.nii.gz')
    WM_file = "%s%s" % (anat_loc, '/WM.nii.gz')
    if anat_loc and not os.path.isfile(CSF_file) and not os.path.isfile(WM_file):
        gen_anat_segs_node = pe.Node(niu.Function(input_names=['anat_loc', 'out_aff'],
                                                  output_names=['new_file_csf', 'mni_csf_loc', 'new_file_wm'],
                                                  function=diffconnectometry.gen_anat_segs, imports=import_list),
                                     name="gen_anat_segs_node")
        no_segs = False
    else:
        no_segs = True
        print('\nRunning tractography without tissue maps. This is not recommended. Consider including a T1/T2 anatomical image with the -anat flag instead.\n')

    prepare_masks_node = pe.Node(niu.Function(input_names=['dwi_dir', 'csf_loc', 'mni_csf_loc', 'wm_mask_loc',
                                                           'mask'],
                                              output_names=['vent_CSF_diff_mask_path', 'way_mask'],
                                              function=diffconnectometry.prepare_masks, imports=import_list),
                                 name="prepare_masks_node")
    prep_nodes_node = pe.Node(niu.Function(input_names=['dwi_dir', 'node_size', 'parc', 'parcel_list',
                                                        'net_parcels_map_nifti', 'network', 'dir_path', 'mask',
                                                        'atlas_select'],
                                           output_names=['parcel_list', 'seeds_dir', 'node_size'],
                                           function=diffconnectometry.prep_nodes, imports=import_list),
                              name="prep_nodes_node")
    if parc is True:
        reg_parcels2diff_node = pe.Node(niu.Function(input_names=['dwi_dir', 'seeds_dir'],
                                                     output_names=['seeds_list'],
                                                     function=diffconnectometry.reg_parcels2diff, imports=import_list),
                                        name="reg_parcels2diff_node")
    else:
        build_coord_list_node = pe.Node(niu.Function(input_names=['dwi_dir', 'coords'],
                                                     output_names=['coords'],
                                                     function=diffconnectometry.build_coord_list, imports=import_list),
                                        name="build_coord_list_node")
        reg_coords2diff_node = pe.Node(niu.Function(input_names=['coords', 'dwi_dir', 'node_size', 'seeds_dir'],
                                                    output_names=['done_nodes'],
                                                    function=diffconnectometry.reg_coords2diff, imports=import_list),
                                       name="reg_coords2diff_node")
        cleanup_tmp_nodes_node = pe.Node(niu.Function(input_names=['done_nodes', 'coords', 'dir_path', 'seeds_dir'],
                                                      output_names=['seeds_list'],
                                                      function=diffconnectometry.cleanup_tmp_nodes, imports=import_list),
                                         name="cleanup_tmp_nodes_node")
    create_seed_mask_file_node = pe.Node(niu.Function(input_names=['node_size', 'network', 'dir_path', 'parc',
                                                                   'seeds_list', 'atlas_select'],
                                                      output_names=['seeds_text', 'probtrackx_output_dir_path'],
                                                      function=diffconnectometry.create_seed_mask_file,
                                                      imports=import_list),
                                         name="create_seed_mask_file_node")
    run_probtrackx2_node = pe.Node(niu.Function(input_names=['i', 'seeds_text', 'dwi_dir',
                                                             'probtrackx_output_dir_path', 'vent_CSF_diff_mask_path',
                                                             'way_mask', 'procmem', 'num_total_samples'],
                                                function=diffconnectometry.run_probtrackx2, imports=import_list),
                                   name="run_probtrackx2_node")
    run_dipy_tracking_node = pe.Node(niu.Function(input_names=['dwi_dir', 'node_size', 'dir_path',
                                                               'conn_model', 'parc', 'atlas_select',
                                                               'network', 'wm_mask'],
                                                  function=diffconnectometry.dwi_dipy_run, imports=import_list),
                                     name="run_dipy_tracking_node")
    collect_struct_mapping_outputs_node = pe.Node(niu.Function(input_names=['parc', 'dwi_dir', 'network', 'ID',
                                                                            'probtrackx_output_dir_path', 'dir_path',
                                                                            'procmem', 'seeds_dir'],
                                                               output_names=['conn_matrix_symm'],
                                                               function=diffconnectometry.collect_struct_mapping_outputs,
                                                               imports=import_list),
                                                  name="collect_struct_mapping_outputs_node")
    thresh_diff_node = pe.Node(niu.Function(input_names=['dens_thresh', 'thr', 'conn_model', 'network', 'ID',
                                                         'dir_path', 'mask', 'node_size', 'conn_matrix', 'parc',
                                                         'min_span_tree'],
                                            output_names=['conn_matrix_thr', 'edge_threshold', 'est_path', 'thr',
                                                          'node_size', 'network', 'conn_model', 'mask'],
                                            function=thresholding.thresh_diff,
                                            imports=import_list), name="thresh_diff_node")
    if plot_switch is True:
        structural_plotting_node = pe.Node(niu.Function(input_names=['conn_matrix_symm', 'label_names', 'atlas_select',
                                                                     'ID', 'dwi_dir', 'network', 'parc', 'coords',
                                                                     'mask', 'dir_path', 'conn_model', 'thr',
                                                                     'node_size'],
                                                        function=plotting.structural_plotting,
                                                        imports=import_list),
                                           name="structural_plotting_node")
    outputnode = pe.JoinNode(interface=niu.IdentityInterface(fields=['est_path', 'thr', 'node_size', 'network',
                                                                     'conn_model']),
                             name='outputnode',
                             joinfield=['est_path', 'thr', 'node_size', 'network', 'conn_model'],
                             joinsource='thresh_diff_node')
    run_probtrackx2_node.interface.n_procs = 1
    run_probtrackx2_node.interface.mem_gb = 2
    run_probtrackx2_iterables = []
    iter_i = range(int(procmem[0]))
    run_probtrackx2_iterables.append(("i", iter_i))
    run_probtrackx2_node.iterables = run_probtrackx2_iterables
    if (multi_atlas is not None and user_atlas_list is None and parlistfile is None) or (multi_atlas is None and atlas_select is None and user_atlas_list is not None):
        flexi_atlas = False
        if multi_atlas is not None and user_atlas_list is None:
            WB_fetch_nodes_and_labels_node_iterables = []
            WB_fetch_nodes_and_labels_node_iterables.append(("atlas_select", multi_atlas))
            WB_fetch_nodes_and_labels_node.iterables = WB_fetch_nodes_and_labels_node_iterables
        elif multi_atlas is None and user_atlas_list is not None:
            WB_fetch_nodes_and_labels_node_iterables = []
            WB_fetch_nodes_and_labels_node_iterables.append(("parlistfile", user_atlas_list))
            WB_fetch_nodes_and_labels_node.iterables = WB_fetch_nodes_and_labels_node_iterables
    elif ((atlas_select is not None and parlistfile is None) or (atlas_select is None and parlistfile is not None)) and (multi_atlas is None and user_atlas_list is None):
        flexi_atlas = False
        pass
    else:
        flexi_atlas = True
        flexi_atlas_source = pe.Node(niu.IdentityInterface(fields=['atlas_select', 'parlistfile']),
                                     name='flexi_atlas_source')
        if multi_atlas is not None and user_atlas_list is not None:
            flexi_atlas_source_iterables = [("atlas_select", len(user_atlas_list) * [None] + multi_atlas),
                                            ("parlistfile", user_atlas_list + len(multi_atlas) * [None])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif multi_atlas is not None and parlistfile is not None and user_atlas_list is None:
            flexi_atlas_source_iterables = [("atlas_select", multi_atlas + [None]),
                                            ("parlistfile", len(multi_atlas) * [None] + [parlistfile])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif atlas_select is not None and user_atlas_list is not None and multi_atlas is None:
            flexi_atlas_source_iterables = [("atlas_select", len(user_atlas_list) * [None] + [atlas_select]),
                                            ("parlistfile", user_atlas_list + [None])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif atlas_select is not None and parlistfile is not None and user_atlas_list is None and multi_atlas is None:
            flexi_atlas_source_iterables = [("atlas_select", [atlas_select, None]),
                                            ("parlistfile", [None, parlistfile])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True

    thresh_diff_node_iterables = []
    if multi_thr is True:
        iter_thresh = sorted(list(set([str(i) for i in np.round(np.arange(float(min_thr),
                                                                          float(max_thr), float(step_thr)),
                                                                decimals=2).tolist()] + [str(float(max_thr))])))
        thresh_diff_node_iterables.append(("thr", iter_thresh))
        if conn_model_list:
            thresh_diff_node_iterables.append(("conn_model", conn_model_list))
        else:
            thresh_diff_node_iterables.append(("conn_model", [conn_model]))
    else:
        if conn_model_list:
            thresh_diff_node_iterables.append(("conn_model", conn_model_list))
            thresh_diff_node_iterables.append(("thr", [thr]))
        else:
            thresh_diff_node_iterables.append(("conn_model", [conn_model]))
            thresh_diff_node_iterables.append(("thr", [thr]))
    thresh_diff_node.iterables = thresh_diff_node_iterables

    if node_size_list and parc is False:
        prep_nodes_node_iterables = []
        prep_nodes_node_iterables.append(("node_size", node_size_list))
        prep_nodes_node.iterables = prep_nodes_node_iterables
    # Connect nodes of workflow
    wb_structural_connectometry_wf.connect([
        (inputnode, WB_fetch_nodes_and_labels_node, [('atlas_select', 'atlas_select'),
                                                     ('parlistfile', 'parlistfile'),
                                                     ('parc', 'parc'),
                                                     ('ref_txt', 'ref_txt'),
                                                     ('use_AAL_naming', 'use_AAL_naming')]),
        (inputnode, node_gen_node, [('ID', 'ID'),
                                    ('mask', 'mask'),
                                    ('parc', 'parc')]),
        (inputnode, WB_fetch_nodes_and_labels_node, [('nodif_brain_mask_path', 'func_file')]),
        (WB_fetch_nodes_and_labels_node, node_gen_node, [('coords', 'coords'),
                                                         ('label_names', 'label_names'),
                                                         ('dir_path', 'dir_path'),
                                                         ('parcel_list', 'parcel_list'),
                                                         ('par_max', 'par_max'),
                                                         ('networks_list', 'networks_list')]),
        (WB_fetch_nodes_and_labels_node, prep_nodes_node, [('parcel_list', 'parcel_list')]),
        (node_gen_node, prep_nodes_node, [('net_parcels_map_nifti', 'net_parcels_map_nifti'),
                                          ('coords', 'coords'),
                                          ('label_names', 'label_names')
                                          ]),
        (inputnode, create_mni2diff_transforms_node, [('dwi_dir', 'dwi_dir')]),
        (WB_fetch_nodes_and_labels_node, prep_nodes_node, [('dir_path', 'dir_path'),
                                                           ('atlas_select', 'atlas_select')]),
        (inputnode, prep_nodes_node, [('dwi_dir', 'dwi_dir'),
                                      ('node_size', 'node_size'),
                                      ('parc', 'parc'),
                                      ('mask', 'mask'),
                                      ('network', 'network')]),
        (inputnode, run_probtrackx2_node, [('dwi_dir', 'dwi_dir'),
                                           ('procmem', 'procmem'),
                                           ('num_total_samples', 'num_total_samples')]),
        (inputnode, create_seed_mask_file_node, [('node_size', 'node_size'), ('parc', 'parc'), ('network', 'network')]),
        (WB_fetch_nodes_and_labels_node, create_seed_mask_file_node, [('dir_path', 'dir_path'),
                                                                      ('atlas_select', 'atlas_select')]),
        (create_seed_mask_file_node, run_probtrackx2_node, [('seeds_text', 'seeds_text'),
                                                            ('probtrackx_output_dir_path','probtrackx_output_dir_path')
                                                            ]),
        (create_seed_mask_file_node, collect_struct_mapping_outputs_node, [('probtrackx_output_dir_path',
                                                                            'probtrackx_output_dir_path')]),
        (WB_fetch_nodes_and_labels_node, collect_struct_mapping_outputs_node, [('dir_path', 'dir_path')]),
        (WB_fetch_nodes_and_labels_node, thresh_diff_node, [('dir_path', 'dir_path')]),
        (inputnode, collect_struct_mapping_outputs_node, [('dwi_dir', 'dwi_dir'),
                                                          ('parc', 'parc'),
                                                          ('network', 'network'),
                                                          ('procmem', 'procmem'),
                                                          ('ID', 'ID')]),
        (prep_nodes_node, collect_struct_mapping_outputs_node, [('node_size', 'node_size'),
                                                                ('seeds_dir', 'seeds_dir')]),
        (inputnode, thresh_diff_node, [('dens_thresh', 'dens_thresh'),
                                       ('thr', 'thr'),
                                       ('network', 'network'),
                                       ('conn_model', 'conn_model'),
                                       ('ID', 'ID'),
                                       ('mask', 'mask'),
                                       ('parc', 'parc'),
                                       ('min_span_tree', 'min_span_tree')]),
        (prep_nodes_node, thresh_diff_node, [('node_size', 'node_size')]),
        (collect_struct_mapping_outputs_node, thresh_diff_node, [('conn_matrix_symm', 'conn_matrix')]),
        (thresh_diff_node, outputnode, [('est_path', 'est_path'),
                                        ('thr', 'thr'),
                                        ('node_size', 'node_size'),
                                        ('network', 'network'),
                                        ('conn_model', 'conn_model')])
        ])
    if no_segs is not True:
        wb_structural_connectometry_wf.add_nodes([gen_anat_segs_node, prepare_masks_node])
        wb_structural_connectometry_wf.connect([(create_mni2diff_transforms_node, gen_anat_segs_node, [('out_aff',
                                                                                                        'out_aff')]),
                                                (inputnode, gen_anat_segs_node, [('anat_loc', 'anat_loc')]),
                                                (inputnode, prepare_masks_node, [('dwi_dir', 'dwi_dir'),
                                                                                 ('mask', 'mask')]),
                                                (gen_anat_segs_node, prepare_masks_node, [('new_file_csf', 'csf_loc'),
                                                                                          ('mni_csf_loc', 'mni_csf_loc'),
                                                                                          ('new_file_wm', 'wm_mask_loc')]),
                                                (prepare_masks_node, run_probtrackx2_node, [('vent_CSF_diff_mask_path',
                                                                                             'vent_CSF_diff_mask_path'),
                                                                                            ('way_mask', 'way_mask')])
                                                ])
    if parc is False:
        wb_structural_connectometry_wf.add_nodes([build_coord_list_node, reg_coords2diff_node, cleanup_tmp_nodes_node])
        wb_structural_connectometry_wf.connect([(inputnode, build_coord_list_node, [('dwi_dir', 'dwi_dir')]),
                                                (WB_fetch_nodes_and_labels_node, build_coord_list_node, [('coords',
                                                                                                          'coords')]),
                                                (prep_nodes_node, reg_coords2diff_node, [('seeds_dir', 'seeds_dir'),
                                                                                         ('node_size', 'node_size')]),
                                                (inputnode, reg_coords2diff_node, [('dwi_dir', 'dwi_dir')]),
                                                (build_coord_list_node, reg_coords2diff_node, [('coords', 'coords')]),
                                                (WB_fetch_nodes_and_labels_node, cleanup_tmp_nodes_node, [('dir_path',
                                                                                                           'dir_path')]),
                                                (reg_coords2diff_node, cleanup_tmp_nodes_node, [('done_nodes',
                                                                                                 'done_nodes')]),
                                                (build_coord_list_node, cleanup_tmp_nodes_node, [('coords', 'coords')]),
                                                (prep_nodes_node, cleanup_tmp_nodes_node, [('seeds_dir', 'seeds_dir')]),
                                                (cleanup_tmp_nodes_node, create_seed_mask_file_node, [('seeds_list',
                                                                                                       'seeds_list')])
                                                ])
    else:
        wb_structural_connectometry_wf.add_nodes([reg_parcels2diff_node])
        wb_structural_connectometry_wf.connect([(inputnode, reg_parcels2diff_node, [('dwi_dir', 'dwi_dir')]),
                                                (prep_nodes_node, reg_parcels2diff_node, [('seeds_dir', 'seeds_dir')]),
                                                (reg_parcels2diff_node, create_seed_mask_file_node, [('seeds_list',
                                                                                                      'seeds_list')])
                                                ])
    if plot_switch is True:
        wb_structural_connectometry_wf.add_nodes([structural_plotting_node])
        wb_structural_connectometry_wf.connect([(collect_struct_mapping_outputs_node, structural_plotting_node,
                                                 [('conn_matrix_symm', 'conn_matrix_symm')]),
                                                (inputnode, structural_plotting_node, [('ID', 'ID'),
                                                                                       ('dwi_dir', 'dwi_dir'),
                                                                                       ('network', 'network'),
                                                                                       ('parc', 'parc'),
                                                                                       ('mask', 'mask'),
                                                                                       ('plot_switch', 'plot_switch')]),
                                                (thresh_diff_node, structural_plotting_node,
                                                 [('thr', 'thr'),
                                                  ('node_size', 'node_size'), ('conn_model', 'conn_model')]),
                                                (node_gen_node, structural_plotting_node,
                                                 [('label_names', 'label_names'),
                                                  ('coords', 'coords')]),
                                                (WB_fetch_nodes_and_labels_node, structural_plotting_node,
                                                 [('dir_path', 'dir_path'),
                                                  ('atlas_select', 'atlas_select')])
                                                ])
    dwi_img = "%s%s" % (dwi_dir, '/dwi.nii.gz')
    nodif_brain_mask_path = "%s%s" % (dwi_dir, '/nodif_brain_mask.nii.gz')
    bvals = "%s%s" % (dwi_dir, '/bval')
    bvecs = "%s%s" % (dwi_dir, '/bvec')
    if '.bedpostX' not in dir_path and os.path.exists(dwi_img) and os.path.exists(bvals) and os.path.exists(bvecs) and os.path.exists(nodif_brain_mask_path):
        wb_structural_connectometry_wf.disconnect(
            (inputnode, run_probtrackx2_node, [('dwi_dir', 'dwi_dir'),
                                               ('procmem', 'procmem'),
                                               ('num_total_samples', 'num_total_samples')]),
            (create_seed_mask_file_node, run_probtrackx2_node, [('seeds_text', 'seeds_text'),
                                                                ('probtrackx_output_dir_path',
                                                                 'probtrackx_output_dir_path')]),
            (prepare_masks_node, run_probtrackx2_node, [('vent_CSF_diff_mask_path', 'vent_CSF_diff_mask_path'),
                                                        ('way_mask', 'way_mask')]),
            (create_seed_mask_file_node, collect_struct_mapping_outputs_node, [('probtrackx_output_dir_path',
                                                                                'probtrackx_output_dir_path')]),
            (WB_fetch_nodes_and_labels_node, collect_struct_mapping_outputs_node, [('dir_path', 'dir_path')]),
            (inputnode, collect_struct_mapping_outputs_node, [('dwi_dir', 'dwi_dir'),
                                                              ('parc', 'parc'),
                                                              ('network', 'network'),
                                                              ('procmem', 'procmem'),
                                                              ('ID', 'ID')]),
            (prep_nodes_node, collect_struct_mapping_outputs_node, [('node_size', 'node_size'),
                                                                    ('seeds_dir', 'seeds_dir')]),
            (collect_struct_mapping_outputs_node, thresh_diff_node, [('conn_matrix_symm', 'conn_matrix')]),
            (collect_struct_mapping_outputs_node, structural_plotting_node, [('conn_matrix_symm',
                                                                              'conn_matrix_symm')]))
        wb_structural_connectometry_wf.connect(
            (inputnode, run_dipy_tracking_node, [('dwi_dir', 'dwi_dir'),
                                                 ('conn_model', 'conn_model'),
                                                 ('network', 'network'),
                                                 ('parc', 'parc')]),
            (create_seed_mask_file_node, run_dipy_tracking_node, [('seeds_text', 'seeds_text'),
                                                                  ('probtrackx_output_dir_path',
                                                                 'probtrackx_output_dir_path')]),
            (prepare_masks_node, run_dipy_tracking_node, [('way_mask', 'wm_mask')]),
            (prep_nodes_node, run_dipy_tracking_node, [('node_size', 'node_size')]),
            (WB_fetch_nodes_and_labels_node, run_dipy_tracking_node, [('atlas_select', 'atlas_select'),
                                                                      ('dir_path', 'dir_path')]),
            (run_dipy_tracking_node, thresh_diff_node, [('conn_matrix', 'conn_matrix')]),
            (run_dipy_tracking_node, structural_plotting_node, [('conn_matrix', 'conn_matrix')]))

    if flexi_atlas is True:
        wb_structural_connectometry_wf.disconnect([(inputnode, WB_fetch_nodes_and_labels_node,
                                                    [('atlas_select', 'atlas_select'), ('parlistfile', 'parlistfile')])
                                                   ])
        wb_structural_connectometry_wf.connect([(flexi_atlas_source, WB_fetch_nodes_and_labels_node,
                                                 [('atlas_select', 'atlas_select'), ('parlistfile', 'parlistfile')])
                                                ])
    wb_structural_connectometry_wf.config['execution']['crashdump_dir'] = wb_structural_connectometry_wf.base_directory
    wb_structural_connectometry_wf.config['execution']['crashfile_format'] = 'txt'
    wb_structural_connectometry_wf.config['logging']['log_directory'] = wb_structural_connectometry_wf.base_directory
    wb_structural_connectometry_wf.config['logging']['workflow_level'] = 'DEBUG'
    wb_structural_connectometry_wf.config['logging']['utils_level'] = 'DEBUG'
    wb_structural_connectometry_wf.config['logging']['interface_level'] = 'DEBUG'
    wb_structural_connectometry_wf.config['execution']['display_variable'] = ':0'

    return wb_structural_connectometry_wf


def rsn_structural_connectometry(ID, atlas_select, network, node_size, mask, parlistfile, plot_switch, parc, ref_txt,
                                 procmem, dir_path, dwi_dir, anat_loc, thr, dens_thresh, conn_model,
                                 user_atlas_list, multi_thr, multi_atlas, max_thr, min_thr, step_thr, node_size_list,
                                 num_total_samples, conn_model_list, min_span_tree, multi_nets, use_AAL_naming):
    import os.path
    from nipype.pipeline import engine as pe
    from nipype.interfaces import utility as niu
    from pynets import nodemaker, diffconnectometry, plotting, thresholding, utils

    nodif_brain_mask_path = "%s%s" % (dwi_dir, '/nodif_brain_mask.nii.gz')

    import_list = ["import sys", "import os", "import numpy as np", "import networkx as nx", "import nibabel as nib"]
    rsn_structural_connectometry_wf = pe.Workflow(name='rsn_structural_connectometry_' + str(ID))
    base_dirname = "%s%s%s%s" % ('wb_structural_connectometry_', str(ID), '/Meta_wf_imp_est_', str(ID))
    rsn_structural_connectometry_wf.base_directory = dwi_dir + base_dirname

    # Create input/output nodes
    # 1) Add variable to IdentityInterface if user-set
    inputnode = pe.Node(niu.IdentityInterface(fields=['ID', 'atlas_select', 'network', 'node_size', 'mask',
                                                      'parlistfile', 'plot_switch', 'parc', 'ref_txt', 'procmem',
                                                      'dir_path', 'dwi_dir', 'anat_loc', 'thr', 'dens_thresh',
                                                      'conn_model', 'user_atlas_list', 'multi_thr', 'multi_atlas',
                                                      'max_thr', 'min_thr', 'step_thr', 'num_total_samples',
                                                      'min_span_tree', 'multi_nets', 'use_AAL_naming']),
                        name='inputnode')

    # 2)Add variable to input nodes if user-set (e.g. inputnode.inputs.WHATEVER)
    inputnode.inputs.ID = ID
    inputnode.inputs.atlas_select = atlas_select
    inputnode.inputs.network = network
    inputnode.inputs.node_size = node_size
    inputnode.inputs.mask = mask
    inputnode.inputs.parlistfile = parlistfile
    inputnode.inputs.plot_switch = plot_switch
    inputnode.inputs.parc = parc
    inputnode.inputs.ref_txt = ref_txt
    inputnode.inputs.procmem = procmem
    inputnode.inputs.dir_path = dir_path
    inputnode.inputs.dwi_dir = dwi_dir
    inputnode.inputs.anat_loc = anat_loc
    inputnode.inputs.nodif_brain_mask_path = nodif_brain_mask_path
    inputnode.inputs.thr = thr
    inputnode.inputs.dens_thresh = dens_thresh
    inputnode.inputs.conn_model = conn_model
    inputnode.inputs.user_atlas_list = user_atlas_list
    inputnode.inputs.multi_thr = multi_thr
    inputnode.inputs.multi_atlas = multi_atlas
    inputnode.inputs.max_thr = max_thr
    inputnode.inputs.min_thr = min_thr
    inputnode.inputs.step_thr = step_thr
    inputnode.inputs.num_total_samples = num_total_samples
    inputnode.inputs.multi_nets = multi_nets
    inputnode.inputs.conn_model_list = conn_model_list
    inputnode.inputs.min_span_tree = min_span_tree
    inputnode.inputs.use_AAL_naming = use_AAL_naming

    # 3) Add variable to function nodes
    # Create function nodes
    RSN_fetch_nodes_and_labels_node = pe.Node(niu.Function(input_names=['atlas_select', 'parlistfile', 'ref_txt',
                                                                        'parc', 'func_file', 'use_AAL_naming'],
                                                           output_names=['label_names', 'coords', 'atlas_select',
                                                                         'networks_list', 'parcel_list', 'par_max',
                                                                         'parlistfile', 'dir_path'],
                                                           function=nodemaker.RSN_fetch_nodes_and_labels,
                                                           imports=import_list), name="RSN_fetch_nodes_and_labels_node")
    get_node_membership_node = pe.Node(niu.Function(input_names=['network', 'func_file', 'coords', 'label_names',
                                                                 'parc', 'parcel_list'],
                                                    output_names=['net_coords', 'net_parcel_list', 'net_label_names',
                                                                  'network'],
                                                    function=nodemaker.get_node_membership, imports=import_list),
                                       name="get_node_membership_node")
    # Node generation
    # if mask is not None:
    #     node_gen_node = pe.Node(niu.Function(input_names=['mask', 'coords', 'parcel_list', 'label_names', 'dir_path', 'ID', 'parc'],
    #                                                  output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
    #                                                  function=nodemaker.node_gen_masking, imports=import_list), name="node_gen_masking_node")
    # else:
    #     node_gen_node = pe.Node(niu.Function(input_names=['coords', 'parcel_list', 'label_names', 'dir_path', 'ID', 'parc'],
    #                                                  output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
    #                                                  function=nodemaker.node_gen, imports=import_list), name="node_gen_node")
    node_gen_node = pe.Node(niu.Function(input_names=['coords', 'parcel_list', 'label_names', 'dir_path', 'ID', 'parc'],
                                         output_names=['net_parcels_map_nifti', 'coords', 'label_names'],
                                         function=nodemaker.node_gen, imports=import_list), name="node_gen_node")
    save_coords_and_labels_node = pe.Node(niu.Function(input_names=['coords', 'label_names', 'dir_path', 'network'],
                                                       function=utils.save_RSN_coords_and_labels_to_pickle,
                                                       imports=import_list), name="save_coords_and_labels_node")
    create_mni2diff_transforms_node = pe.Node(niu.Function(input_names=['dwi_dir'], output_names=['out_aff'],
                                                           function=diffconnectometry.create_mni2diff_transforms,
                                                           imports=import_list), name="create_mni2diff_transforms_node")
    CSF_file = "%s%s" % (anat_loc, '/CSF.nii.gz')
    WM_file = "%s%s" % (anat_loc, '/WM.nii.gz')
    if anat_loc and not os.path.isfile(CSF_file) and not os.path.isfile(WM_file):
        gen_anat_segs_node = pe.Node(niu.Function(input_names=['anat_loc', 'out_aff'],
                                                  output_names=['new_file_csf', 'mni_csf_loc', 'new_file_wm'],
                                                  function=diffconnectometry.gen_anat_segs, imports=import_list),
                                     name="gen_anat_segs_node")
        no_segs = False
    else:
        no_segs = True
        print(
            '\nRunning tractography without tissue maps. This is not recommended. Consider including a T1/T2 anatomical image with the -anat flag instead.\n')

    prepare_masks_node = pe.Node(niu.Function(input_names=['dwi_dir', 'csf_loc', 'mni_csf_loc', 'wm_mask_loc',
                                                           'mask'],
                                              output_names=['vent_CSF_diff_mask_path', 'way_mask'],
                                              function=diffconnectometry.prepare_masks, imports=import_list),
                                 name="prepare_masks_node")
    prep_nodes_node = pe.Node(niu.Function(input_names=['dwi_dir', 'node_size', 'parc', 'parcel_list',
                                                        'net_parcels_map_nifti', 'network', 'dir_path', 'mask',
                                                        'atlas_select'],
                                           output_names=['parcel_list', 'seeds_dir', 'node_size'],
                                           function=diffconnectometry.prep_nodes, imports=import_list),
                              name="prep_nodes_node")
    if parc is True:
        reg_parcels2diff_node = pe.Node(niu.Function(input_names=['dwi_dir', 'seeds_dir'],
                                                     output_names=['seeds_list'],
                                                     function=diffconnectometry.reg_parcels2diff, imports=import_list),
                                        name="reg_parcels2diff_node")
    else:
        build_coord_list_node = pe.Node(niu.Function(input_names=['dwi_dir', 'coords'],
                                                     output_names=['coords'],
                                                     function=diffconnectometry.build_coord_list, imports=import_list),
                                        name="build_coord_list_node")
        reg_coords2diff_node = pe.Node(niu.Function(input_names=['coords', 'dwi_dir', 'node_size', 'seeds_dir'],
                                                    output_names=['done_nodes'],
                                                    function=diffconnectometry.reg_coords2diff, imports=import_list),
                                       name="reg_coords2diff_node")
        cleanup_tmp_nodes_node = pe.Node(
            niu.Function(input_names=['done_nodes', 'coords', 'dir_path', 'seeds_dir'],
                         output_names=['seeds_list'],
                         function=diffconnectometry.cleanup_tmp_nodes, imports=import_list),
            name="cleanup_tmp_nodes_node")
    create_seed_mask_file_node = pe.Node(niu.Function(input_names=['node_size', 'network', 'dir_path', 'parc',
                                                                   'seeds_list', 'atlas_select'],
                                                      output_names=['seeds_text', 'probtrackx_output_dir_path'],
                                                      function=diffconnectometry.create_seed_mask_file,
                                                      imports=import_list),
                                         name="create_seed_mask_file_node")
    run_probtrackx2_node = pe.Node(niu.Function(input_names=['i', 'seeds_text', 'dwi_dir',
                                                             'probtrackx_output_dir_path', 'vent_CSF_diff_mask_path',
                                                             'way_mask', 'procmem', 'num_total_samples'],
                                                function=diffconnectometry.run_probtrackx2, imports=import_list),
                                   name="run_probtrackx2_node")
    run_dipy_tracking_node = pe.Node(niu.Function(input_names=['dwi_dir', 'node_size', 'dir_path',
                                                               'conn_model', 'parc', 'atlas_select',
                                                               'network', 'wm_mask'],
                                                  function=diffconnectometry.dwi_dipy_run, imports=import_list),
                                     name="run_dipy_tracking_node")
    collect_struct_mapping_outputs_node = pe.Node(niu.Function(input_names=['parc', 'dwi_dir', 'network', 'ID',
                                                                            'probtrackx_output_dir_path', 'dir_path',
                                                                            'procmem', 'seeds_dir'],
                                                               output_names=['conn_matrix_symm'],
                                                               function=diffconnectometry.collect_struct_mapping_outputs,
                                                               imports=import_list),
                                                  name="collect_struct_mapping_outputs_node")
    thresh_diff_node = pe.Node(niu.Function(input_names=['dens_thresh', 'thr', 'conn_model', 'network', 'ID',
                                                         'dir_path', 'mask', 'node_size', 'conn_matrix', 'parc',
                                                         'min_span_tree'],
                                            output_names=['conn_matrix_thr', 'edge_threshold', 'est_path', 'thr',
                                                          'node_size', 'network', 'conn_model', 'mask'],
                                            function=thresholding.thresh_diff,
                                            imports=import_list), name="thresh_diff_node")
    if plot_switch is True:
        structural_plotting_node = pe.Node(niu.Function(input_names=['conn_matrix_symm', 'label_names', 'atlas_select',
                                                                     'ID', 'dwi_dir', 'network', 'parc', 'coords',
                                                                     'mask', 'dir_path', 'conn_model', 'thr',
                                                                     'node_size'],
                                                        function=plotting.structural_plotting,
                                                        imports=import_list),
                                           name="structural_plotting_node")
    outputnode = pe.JoinNode(interface=niu.IdentityInterface(fields=['est_path', 'thr', 'node_size', 'network',
                                                                     'conn_model']),
                             name='outputnode',
                             joinfield=['est_path', 'thr', 'node_size', 'network', 'conn_model'],
                             joinsource='thresh_diff_node')
    run_probtrackx2_node.interface.n_procs = 1
    run_probtrackx2_node.interface.mem_gb = 2
    run_probtrackx2_iterables = []
    iter_i = range(int(procmem[0]))
    run_probtrackx2_iterables.append(("i", iter_i))
    run_probtrackx2_node.iterables = run_probtrackx2_iterables
    if (multi_atlas is not None and user_atlas_list is None and parlistfile is None) or (multi_atlas is None and atlas_select is None and user_atlas_list is not None):
        flexi_atlas = False
        if multi_atlas is not None and user_atlas_list is None:
            RSN_fetch_nodes_and_labels_node_iterables = []
            RSN_fetch_nodes_and_labels_node_iterables.append(("atlas_select", multi_atlas))
            RSN_fetch_nodes_and_labels_node.iterables = RSN_fetch_nodes_and_labels_node_iterables
        elif multi_atlas is None and user_atlas_list is not None:
            RSN_fetch_nodes_and_labels_node_iterables = []
            RSN_fetch_nodes_and_labels_node_iterables.append(("parlistfile", user_atlas_list))
            RSN_fetch_nodes_and_labels_node.iterables = RSN_fetch_nodes_and_labels_node_iterables
    elif ((atlas_select is not None and parlistfile is None) or (atlas_select is None and parlistfile is not None)) and (multi_atlas is None and user_atlas_list is None):
        flexi_atlas = False
        pass
    else:
        flexi_atlas = True
        flexi_atlas_source = pe.Node(niu.IdentityInterface(fields=['atlas_select', 'parlistfile']),
                                     name='flexi_atlas_source')
        if multi_atlas is not None and user_atlas_list is not None:
            flexi_atlas_source_iterables = [("atlas_select", len(user_atlas_list) * [None] + multi_atlas),
                                            ("parlistfile", user_atlas_list + len(multi_atlas) * [None])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif multi_atlas is not None and parlistfile is not None and user_atlas_list is None:
            flexi_atlas_source_iterables = [("atlas_select", multi_atlas + [None]),
                                            ("parlistfile", len(multi_atlas) * [None] + [parlistfile])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif atlas_select is not None and user_atlas_list is not None and multi_atlas is None:
            flexi_atlas_source_iterables = [("atlas_select", len(user_atlas_list) * [None] + [atlas_select]),
                                            ("parlistfile", user_atlas_list + [None])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True
        elif atlas_select is not None and parlistfile is not None and user_atlas_list is None and multi_atlas is None:
            flexi_atlas_source_iterables = [("atlas_select", [atlas_select, None]),
                                            ("parlistfile", [None, parlistfile])]
            flexi_atlas_source.iterables = flexi_atlas_source_iterables
            flexi_atlas_source.synchronize = True

    if multi_nets is not None:
        get_node_membership_node_iterables = []
        network_iterables = ("network", multi_nets)
        get_node_membership_node_iterables.append(network_iterables)
        get_node_membership_node.iterables = get_node_membership_node_iterables

    thresh_diff_node_iterables = []
    if multi_thr is True:
        iter_thresh = sorted(list(set([str(i) for i in np.round(np.arange(float(min_thr),
                                                                          float(max_thr), float(step_thr)),
                                                                decimals=2).tolist()] + [str(float(max_thr))])))
        thresh_diff_node_iterables.append(("thr", iter_thresh))
        if conn_model_list:
            thresh_diff_node_iterables.append(("conn_model", conn_model_list))
        else:
            thresh_diff_node_iterables.append(("conn_model", [conn_model]))
    else:
        if conn_model_list:
            thresh_diff_node_iterables.append(("conn_model", conn_model_list))
            thresh_diff_node_iterables.append(("thr", [thr]))
        else:
            thresh_diff_node_iterables.append(("conn_model", [conn_model]))
            thresh_diff_node_iterables.append(("thr", [thr]))
    thresh_diff_node.iterables = thresh_diff_node_iterables

    if node_size_list and parc is False:
        prep_nodes_node_iterables = []
        prep_nodes_node_iterables.append(("node_size", node_size_list))
        prep_nodes_node.iterables = prep_nodes_node_iterables
    # Connect nodes of workflow
    rsn_structural_connectometry_wf.connect([
        (inputnode, RSN_fetch_nodes_and_labels_node, [('atlas_select', 'atlas_select'),
                                                      ('parlistfile', 'parlistfile'),
                                                      ('parc', 'parc'),
                                                      ('ref_txt', 'ref_txt'),
                                                      ('use_AAL_naming', 'use_AAL_naming')]),
        (inputnode, get_node_membership_node, [('network', 'network'),
                                               ('nodif_brain_mask_path', 'func_file'),
                                               ('parc', 'parc')]),
        (RSN_fetch_nodes_and_labels_node, get_node_membership_node, [('coords', 'coords'),
                                                                     ('label_names', 'label_names'),
                                                                     ('parcel_list', 'parcel_list'),
                                                                     ('par_max', 'par_max'),
                                                                     ('networks_list', 'networks_list')]),
        (inputnode, node_gen_node, [('ID', 'ID'),
                                    ('mask', 'mask'),
                                    ('parc', 'parc')]),
        (inputnode, RSN_fetch_nodes_and_labels_node, [('nodif_brain_mask_path', 'func_file')]),
        (RSN_fetch_nodes_and_labels_node, node_gen_node, [('dir_path', 'dir_path')]),
        (get_node_membership_node, node_gen_node, [('net_coords', 'coords'),
                                                   ('net_label_names', 'label_names'),
                                                   ('net_parcel_list', 'parcel_list')]),
        (get_node_membership_node, save_coords_and_labels_node, [('net_coords', 'coords'),
                                                                 ('net_label_names', 'label_names'),
                                                                 ('network', 'network')]),
        (RSN_fetch_nodes_and_labels_node, save_coords_and_labels_node, [('dir_path', 'dir_path')]),
        (RSN_fetch_nodes_and_labels_node, prep_nodes_node, [('parcel_list', 'parcel_list')]),
        (node_gen_node, prep_nodes_node, [('net_parcels_map_nifti', 'net_parcels_map_nifti'),
                                          ('coords', 'coords'),
                                          ('label_names', 'label_names')
                                          ]),
        (inputnode, create_mni2diff_transforms_node, [('dwi_dir', 'dwi_dir')]),
        (RSN_fetch_nodes_and_labels_node, prep_nodes_node, [('dir_path', 'dir_path'),
                                                            ('atlas_select', 'atlas_select')]),
        (inputnode, prep_nodes_node, [('dwi_dir', 'dwi_dir'),
                                      ('node_size', 'node_size'),
                                      ('parc', 'parc'),
                                      ('mask', 'mask')]),
        (get_node_membership_node, prep_nodes_node, [('network', 'network')]),
        (inputnode, run_probtrackx2_node, [('dwi_dir', 'dwi_dir'),
                                           ('procmem', 'procmem'),
                                           ('num_total_samples', 'num_total_samples')]),
        (inputnode, create_seed_mask_file_node, [('node_size', 'node_size'), ('parc', 'parc'), ('network', 'network')]),
        (RSN_fetch_nodes_and_labels_node, create_seed_mask_file_node, [('dir_path', 'dir_path'),
                                                                       ('atlas_select', 'atlas_select')]),
        (create_seed_mask_file_node, run_probtrackx2_node, [('seeds_text', 'seeds_text'),
                                                            ('probtrackx_output_dir_path', 'probtrackx_output_dir_path')
                                                            ]),
        (create_seed_mask_file_node, collect_struct_mapping_outputs_node, [('probtrackx_output_dir_path',
                                                                            'probtrackx_output_dir_path')]),
        (RSN_fetch_nodes_and_labels_node, collect_struct_mapping_outputs_node, [('dir_path', 'dir_path')]),
        (RSN_fetch_nodes_and_labels_node, thresh_diff_node, [('dir_path', 'dir_path')]),
        (inputnode, collect_struct_mapping_outputs_node, [('dwi_dir', 'dwi_dir'),
                                                          ('parc', 'parc'),
                                                          ('procmem', 'procmem'),
                                                          ('ID', 'ID')]),
        (get_node_membership_node, collect_struct_mapping_outputs_node, [('network', 'network')]),
        (prep_nodes_node, collect_struct_mapping_outputs_node, [('node_size', 'node_size'),
                                                                ('seeds_dir', 'seeds_dir')]),
        (inputnode, thresh_diff_node, [('dens_thresh', 'dens_thresh'),
                                       ('thr', 'thr'),
                                       ('conn_model', 'conn_model'),
                                       ('ID', 'ID'),
                                       ('mask', 'mask'),
                                       ('parc', 'parc'),
                                       ('min_span_tree', 'min_span_tree')]),
        (get_node_membership_node, thresh_diff_node, [('network', 'network')]),
        (prep_nodes_node, thresh_diff_node, [('node_size', 'node_size')]),
        (collect_struct_mapping_outputs_node, thresh_diff_node, [('conn_matrix_symm', 'conn_matrix')]),
        (thresh_diff_node, outputnode, [('est_path', 'est_path'),
                                        ('thr', 'thr'),
                                        ('node_size', 'node_size'),
                                        ('network', 'network'),
                                        ('conn_model', 'conn_model')])
    ])
    if no_segs is not True:
        rsn_structural_connectometry_wf.add_nodes([gen_anat_segs_node, prepare_masks_node])
        rsn_structural_connectometry_wf.connect(
            [(create_mni2diff_transforms_node, gen_anat_segs_node, [('out_aff', 'out_aff')]),
             (inputnode, gen_anat_segs_node, [('anat_loc', 'anat_loc')]),
             (inputnode, prepare_masks_node, [('dwi_dir', 'dwi_dir'),
                                              ('mask', 'mask')]),
             (gen_anat_segs_node, prepare_masks_node, [('new_file_csf', 'csf_loc'),
                                                       ('mni_csf_loc', 'mni_csf_loc'),
                                                       ('new_file_wm', 'wm_mask_loc')]),
             (prepare_masks_node, run_probtrackx2_node, [('vent_CSF_diff_mask_path', 'vent_CSF_diff_mask_path'),
                                                         ('way_mask', 'way_mask')])
             ])
    if parc is False:
        rsn_structural_connectometry_wf.add_nodes([build_coord_list_node, reg_coords2diff_node, cleanup_tmp_nodes_node])
        rsn_structural_connectometry_wf.connect([(inputnode, build_coord_list_node, [('dwi_dir', 'dwi_dir')]),
                                                 (RSN_fetch_nodes_and_labels_node, build_coord_list_node,
                                                  [('coords', 'coords')]),
                                                 (prep_nodes_node, reg_coords2diff_node, [('seeds_dir', 'seeds_dir'),
                                                                                         ('node_size', 'node_size')]),
                                                 (inputnode, reg_coords2diff_node, [('dwi_dir', 'dwi_dir')]),
                                                 (build_coord_list_node, reg_coords2diff_node, [('coords', 'coords')]),
                                                 (RSN_fetch_nodes_and_labels_node, cleanup_tmp_nodes_node,
                                                  [('dir_path', 'dir_path')]),
                                                 (reg_coords2diff_node, cleanup_tmp_nodes_node,
                                                  [('done_nodes', 'done_nodes')]),
                                                 (build_coord_list_node, cleanup_tmp_nodes_node, [('coords', 'coords')]),
                                                 (prep_nodes_node, cleanup_tmp_nodes_node,
                                                  [('seeds_dir', 'seeds_dir')]),
                                                 (cleanup_tmp_nodes_node, create_seed_mask_file_node,
                                                  [('seeds_list', 'seeds_list')])
                                                 ])
    else:
        rsn_structural_connectometry_wf.add_nodes([reg_parcels2diff_node])
        rsn_structural_connectometry_wf.connect([(inputnode, reg_parcels2diff_node, [('dwi_dir', 'dwi_dir')]),
                                                 (prep_nodes_node, reg_parcels2diff_node,
                                                  [('seeds_dir', 'seeds_dir')]),
                                                 (reg_parcels2diff_node, create_seed_mask_file_node,
                                                  [('seeds_list', 'seeds_list')])
                                                 ])
    if multi_nets is not None:
        if plot_switch is True:
            rsn_structural_connectometry_wf.add_nodes([structural_plotting_node])
            rsn_structural_connectometry_wf.connect([(collect_struct_mapping_outputs_node, structural_plotting_node,
                                                      [('conn_matrix_symm', 'conn_matrix_symm')]),
                                                     (inputnode, structural_plotting_node, [('ID', 'ID'),
                                                                                            ('dwi_dir', 'dwi_dir'),
                                                                                            ('parc', 'parc'),
                                                                                            ('mask', 'mask'),
                                                                                            ('plot_switch', 'plot_switch')]),
                                                     (get_node_membership_node, structural_plotting_node,
                                                      [('network', 'network')]),
                                                     (thresh_diff_node, structural_plotting_node,
                                                      [('thr', 'thr'),
                                                       ('node_size', 'node_size'), ('conn_model', 'conn_model')]),
                                                     (node_gen_node, structural_plotting_node,
                                                      [('label_names', 'label_names'),
                                                       ('coords', 'coords')]),
                                                     (RSN_fetch_nodes_and_labels_node, structural_plotting_node,
                                                      [('dir_path', 'dir_path'),
                                                       ('atlas_select', 'atlas_select')])
                                                     ])

    dwi_img = "%s%s" % (dwi_dir, '/dwi.nii.gz')
    nodif_brain_mask_path = "%s%s" % (dwi_dir, '/nodif_brain_mask.nii.gz')
    bvals = "%s%s" % (dwi_dir, '/bval')
    bvecs = "%s%s" % (dwi_dir, '/bvec')
    if '.bedpostX' not in dir_path and os.path.exists(dwi_img) and os.path.exists(bvals) and os.path.exists(bvecs) and os.path.exists(nodif_brain_mask_path):
        rsn_structural_connectometry_wf.disconnect(
            (inputnode, run_probtrackx2_node, [('dwi_dir', 'dwi_dir'),
                                               ('procmem', 'procmem'),
                                               ('num_total_samples', 'num_total_samples')]),
            (create_seed_mask_file_node, run_probtrackx2_node, [('seeds_text', 'seeds_text'),
                                                                ('probtrackx_output_dir_path',
                                                                 'probtrackx_output_dir_path')]),
            (prepare_masks_node, run_probtrackx2_node, [('vent_CSF_diff_mask_path', 'vent_CSF_diff_mask_path'),
                                                        ('way_mask', 'way_mask')]),
            (create_seed_mask_file_node, collect_struct_mapping_outputs_node, [('probtrackx_output_dir_path',
                                                                                'probtrackx_output_dir_path')]),
            (RSN_fetch_nodes_and_labels_node, collect_struct_mapping_outputs_node, [('dir_path', 'dir_path')]),
            (inputnode, collect_struct_mapping_outputs_node, [('dwi_dir', 'dwi_dir'),
                                                              ('parc', 'parc'),
                                                              ('procmem', 'procmem'),
                                                              ('ID', 'ID')]),
            (get_node_membership_node, collect_struct_mapping_outputs_node, [('network', 'network')]),
            (prep_nodes_node, collect_struct_mapping_outputs_node, [('node_size', 'node_size'),
                                                                    ('seeds_dir', 'seeds_dir')]),
            (collect_struct_mapping_outputs_node, thresh_diff_node, [('conn_matrix_symm', 'conn_matrix')]),
            (collect_struct_mapping_outputs_node, structural_plotting_node, [('conn_matrix_symm',
                                                                              'conn_matrix_symm')]))
        rsn_structural_connectometry_wf.connect(
            (inputnode, run_dipy_tracking_node, [('dwi_dir', 'dwi_dir'),
                                                 ('conn_model', 'conn_model'),
                                                 ('parc', 'parc')]),
            (get_node_membership_node, run_dipy_tracking_node, [('network', 'network')]),
            (create_seed_mask_file_node, run_dipy_tracking_node, [('seeds_text', 'seeds_text'),
                                                                  ('probtrackx_output_dir_path',
                                                                   'probtrackx_output_dir_path')]),
            (prepare_masks_node, run_dipy_tracking_node, [('way_mask', 'wm_mask')]),
            (prep_nodes_node, run_dipy_tracking_node, [('node_size', 'node_size')]),
            (RSN_fetch_nodes_and_labels_node, run_dipy_tracking_node, [('atlas_select', 'atlas_select'),
                                                                       ('dir_path', 'dir_path')]),
            (run_dipy_tracking_node, thresh_diff_node, [('conn_matrix', 'conn_matrix')]),
            (run_dipy_tracking_node, structural_plotting_node, [('conn_matrix', 'conn_matrix')]))
    if flexi_atlas is True:
        rsn_structural_connectometry_wf.disconnect([(inputnode, RSN_fetch_nodes_and_labels_node,
                                                    [('atlas_select', 'atlas_select'), ('parlistfile', 'parlistfile')])
                                                    ])
        rsn_structural_connectometry_wf.connect([(flexi_atlas_source, RSN_fetch_nodes_and_labels_node,
                                                 [('atlas_select', 'atlas_select'), ('parlistfile', 'parlistfile')])
                                                 ])
    rsn_structural_connectometry_wf.config['execution']['crashdump_dir'] = rsn_structural_connectometry_wf.base_directory
    rsn_structural_connectometry_wf.config['execution']['crashfile_format'] = 'txt'
    rsn_structural_connectometry_wf.config['logging']['log_directory'] = rsn_structural_connectometry_wf.base_directory
    rsn_structural_connectometry_wf.config['logging']['workflow_level'] = 'DEBUG'
    rsn_structural_connectometry_wf.config['logging']['utils_level'] = 'DEBUG'
    rsn_structural_connectometry_wf.config['logging']['interface_level'] = 'DEBUG'
    rsn_structural_connectometry_wf.config['execution']['display_variable'] = ':0'

    return rsn_structural_connectometry_wf
