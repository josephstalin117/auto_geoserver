colorEntryMap = {
    'blackodor': {
        'type': 'ramp',
        '-': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#FF0000', 'quantity': '1', 'label': 'blackodor', 'opacity': '1'},
            {'color': '#0000FF', 'quantity': '2', 'label': 'nwater', 'opacity': '1'}
        ]
    },
    'bufferstrip': {
        'type': 'ramp',
        '-': [
            # {'color': '#0000FF', 'quantity': '0', 'label': 'water', 'opacity': '0'},
            # {'color': '#ff8406', 'quantity': '1', 'label': 'city', 'opacity': '1'},
            # {'color': '#22dd00', 'quantity': '2', 'label': 'veg', 'opacity': '1'},
            # {'color': '#00ffe7', 'quantity': '3', 'label': 'soi', 'opacity': '1'},
            # {'color': '#00ff00', 'quantity': '4', 'label': 'crop', 'opacity': '1'}
            {'color': '#0000FF', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0000FF', 'quantity': '1', 'label': 'water', 'opacity': '1'},
            {'color': '#ff8406', 'quantity': '2', 'label': 'city', 'opacity': '1'},
            {'color': '#22dd00', 'quantity': '3', 'label': 'veg', 'opacity': '1'},
            {'color': '#00ffe7', 'quantity': '4', 'label': 'soil', 'opacity': '1'}
        ]
    },
    'landcover': {
        'type': 'ramp',
        '-': [
            {'color': '#0000FF', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0000FF', 'quantity': '1', 'label': 'water', 'opacity': '1'},
            {'color': '#ff8406', 'quantity': '2', 'label': 'city', 'opacity': '1'},
            {'color': '#22dd00', 'quantity': '3', 'label': 'veg', 'opacity': '1'},
            {'color': '#00ffe7', 'quantity': '4', 'label': 'soil', 'opacity': '1'}
        ]
    },
    'inversion': {
        'type': 'ramp',
        '131082_BOD5_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '4', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '8', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '12', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '16', 'label': '16mg/L', 'opacity': '1'}
        ],
        '131082_Chla_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.001', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.1', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '0.2', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '0.3', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '0.4', 'label': '0.4mg/L', 'opacity': '1'}
        ],
        '131082_COD_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '20', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '40', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '60', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '80', 'label': '80mg/L', 'opacity': '1'}
        ],
        '131082_CODMn_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '3', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '6', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '9', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '12', 'label': '12mg/L', 'opacity': '1'}
        ],
        '131082_DO_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#FE0302', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#FEBD01', 'quantity': '5', 'label': '', 'opacity': '1'},
            {'color': '#7FFF78', 'quantity': '9', 'label': '', 'opacity': '1'},
            {'color': '#26AAFF', 'quantity': '13', 'label': '', 'opacity': '1'},
            {'color': '#030fED', 'quantity': '17', 'label': '17mg/L', 'opacity': '1'}
        ],
        '131082_NH3N_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.7', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '1.4', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '2.1', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '2.7', 'label': '2.7mg/L', 'opacity': '1'}
        ],
        '131082_PH_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#F5A472', 'quantity': '7.7', 'label': '7.7', 'opacity': '1'},
            {'color': '#BAC74F', 'quantity': '7.8', 'label': '', 'opacity': '1'},
            {'color': '#45E603', 'quantity': '7.9', 'label': '', 'opacity': '1'},
            {'color': '#37F1A6', 'quantity': '8.0', 'label': '', 'opacity': '1'},
            {'color': '#6FB6FF', 'quantity': '8.2', 'label': '8.2', 'opacity': '1'}
        ],
        '131082_SSC_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '10', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '20', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '30', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '43', 'label': '43mg/L', 'opacity': '1'}
        ],
        '131082_TN_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '5', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '10', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '16', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '22', 'label': '22mg/L', 'opacity': '1'}
        ],
        '131082_TP_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.1', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '0.2', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '0.3', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '0.36', 'label': '0.36mg/L', 'opacity': '1'}
        ],
        '131082_TU_2019-11-04': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0NTU', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '1.5', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '3', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '4.5', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '5.3', 'label': '5.3NTU', 'opacity': '1'}
        ],
        '131082_BOD5_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '4', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '8', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '12', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '15', 'label': '15mg/L', 'opacity': '1'}
        ],
        '131082_Chla_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.001', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.15', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '0.3', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '0.45', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '0.58', 'label': '0.58mg/L', 'opacity': '1'}
        ],
        '131082_COD_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '9', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '18', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '27', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '37', 'label': '37mg/L', 'opacity': '1'}
        ],
        '131082_CODMn_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '4', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '9', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '13', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '17', 'label': '17mg/L', 'opacity': '1'}
        ],
        '131082_NH3N_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.3', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '0.6', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '0.9', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '1.26', 'label': '1.26mg/L', 'opacity': '1'}
        ],
        '131082_PH_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '7.29', 'label': '7.29', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '7.9', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '8.6', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '9.3', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '10', 'label': '10', 'opacity': '1'}
        ],
        '131082_SSC_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '25', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '45', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '65', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '85.7', 'label': '85.7mg/L', 'opacity': '1'}
        ],
        '131082_TN_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '6', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '13', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '19', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '25', 'label': '25mg/L', 'opacity': '1'}
        ],
        '131082_TP_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.1', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '0.2', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '0.3', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '0.36', 'label': '0.36mg/L', 'opacity': '1'}
        ],
        '131082_TU_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0NTU', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '1', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '1.8', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '2.6', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '3.4', 'label': '3.4NTU', 'opacity': '1'}
        ],
        '131082_DO_2019-11-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#F90e00', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#FDC100', 'quantity': '6', 'label': '', 'opacity': '1'},
            {'color': '#B6FF87', 'quantity': '12', 'label': '', 'opacity': '1'},
            {'color': '#22B1FD', 'quantity': '18', 'label': '', 'opacity': '1'},
            {'color': '#0a0aFB', 'quantity': '24.5', 'label': '24.5mg/L', 'opacity': '1'}
        ],
        '131082_BOD5_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '4', 'label': '4mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '5', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '6', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '7', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '8', 'label': '8mg/L', 'opacity': '1'}
        ],
        '131082_Chla_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.001', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.07', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '0.13', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '0.2', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '0.27', 'label': '0.27mg/L', 'opacity': '1'}
        ],
        '131082_COD_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '8.5', 'label': '8.5mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '14', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '20', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '25', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '30', 'label': '30mg/L', 'opacity': '1'}
        ],
        '131082_CODMn_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '1.5', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '3', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '4.5', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '6', 'label': '6mg/L', 'opacity': '1'}
        ],
        '131082_NH3N_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '1.8', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '3.6', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '5.4', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '7.2', 'label': '7.2mg/L', 'opacity': '1'}
        ],
        '131082_SSC_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '10', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '20', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '30', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '40', 'label': '40mg/L', 'opacity': '1'}
        ],
        '131082_TN_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.75', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '1.5', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '2.25', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '3', 'label': '3mg/L', 'opacity': '1'}
        ],
        '131082_TP_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0mg/L', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '0.06', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '0.12', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '0.18', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '0.25', 'label': '0.25mg/L', 'opacity': '1'}
        ],
        '131082_TU_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '0.01', 'label': '0NTU', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '1.5', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '3', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '4', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '5.5', 'label': '5.5NTU', 'opacity': '1'}
        ],
        '131082_DO_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#F90e00', 'quantity': '4', 'label': '4mg/L', 'opacity': '1'},
            {'color': '#FDC100', 'quantity': '7', 'label': '', 'opacity': '1'},
            {'color': '#B6FF87', 'quantity': '10', 'label': '', 'opacity': '1'},
            {'color': '#22B1FD', 'quantity': '13', 'label': '', 'opacity': '1'},
            {'color': '#0a0aFB', 'quantity': '16.5', 'label': '16.5mg/L', 'opacity': '1'}
        ],
        '131082_PH_2020-09-19': [
            {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
            {'color': '#0f0eF5', 'quantity': '7.5', 'label': '7.5', 'opacity': '1'},
            {'color': '#24ABFD', 'quantity': '7.65', 'label': '', 'opacity': '1'},
            {'color': '#87FE7D', 'quantity': '7.8', 'label': '', 'opacity': '1'},
            {'color': '#FEC200', 'quantity': '8.0', 'label': '', 'opacity': '1'},
            {'color': '#FF1800', 'quantity': '8.2', 'label': '8.2', 'opacity': '1'}
        ]
    }
}
