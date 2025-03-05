def replacePayload(payload):
    keyMap = {
        # Query Object
        'term': 'termo',
        'mainActivity': 'atividade_principal',
        'legalNature': 'natureza_juridica',
        'uf': 'uf',
        'municipality': 'municipio',
        'neighborhood': 'bairro',
        'registrationSituation': 'situacao_cadastral',
        'postalCode': 'cep',
        'ddd': 'ddd',

        'Active': 'ATIVO',
        'Low': 'BAIXADA',
        'Unfit': 'INAPTA',
        'Suspended': 'SUSPENSA',

        # RangeQuery Object
        'rangeQuery': 'range_query',
        'openingDate': 'data_abertura',
        'shareCapital': 'capital_social',

        # Extras Object
        'withTelephoneContact': 'com_contato_telefonico',
        'withEmail': 'com_email',
        'deleteMei': 'excluir_mei',
        'includeSecondaryActivity': 'incluir_atividade_secundaria',
        'onlyCellNumber': 'somente_celular',
        'onlyBranch': 'somente_filial',
        'onlyLandline': 'somente_fixo',
        'onlyHeadquarters': 'somente_matriz',
        'onlyMei': 'somente_mei'
    }

    newPayload = {}
    for key, value in payload.items():
        newKey = keyMap.get(key, key)

        if isinstance(value, dict):
            newPayload[newKey] = replacePayload(value)
        else:
            newPayload[newKey] = value
    
    return newPayload