import pandas as pd
from database_sql import get_inventory

# Variaables
locations_870 = ['870', '870-1', '870-2', '870-3', '870-4', '870-5', '870-6']
locations_940 = ['940', '940.2', '940.4', 'Dirty Totes', 'Drop for 870', 'Jaco Grinding',
                'Pregrinds', 'Pregrinds 2', 'Pregrinds 3', 'Pregrinds 4',
                'Storage System 3', 'System 1 Hopper', 'Zone A', 'Zone B',
                'Zone C', 'Zone D', 'Zone E']


# Filter by location
def filter_location(location, df):
    if location == 'rave':
        filtered = df['location'].isin(locations_870)
    elif location == 'jaco':
        filtered = df['location'].isin(locations_940)
    else:
        return df

    df = df[ filtered ]
    return df


# Find Ingredients with Multiple Totes
def find_multiples(df):
    products = []
    product_list = []
    for product in df['gmc']:
        products.append(product)

    for product in products:
        count = products.count(product)
        if product not in product_list and count > 1:
            product_list.append(product)

    return product_list


# Filter multiple totes
def filter_multiples(df, multiples):
    filtered = df['gmc'].isin(multiples)
    df = df[ filtered ]

    return df


# Check if weights can be combined
def check_matches(df, multiples):
    matches = []

    for product in multiples:
        totes = df.loc[df['gmc'] == product]
        matches.append(totes)

    return matches

# Check if weights can be combined
def check_mergable(matches):
    consolidations = []
    for match in matches:
        added_list = []
        for i, tote in match.iterrows():
            for j, compTote in match.iterrows():
                if tote['batch'] != compTote['batch']:
                    if (tote['weight'] + compTote['weight']) < 1850:
                        added_list.append(compTote.to_dict())
        
        added_list = sorted(added_list, key=lambda x: x['weight'])

        if len(added_list) > 0:
            consolidations.append(added_list)

    consolidations = sorted(consolidations, key=lambda x: x[0]['color'])
    return consolidations

# Get Consolidations
def get_consolidations(location):
    df = get_inventory()
    df = filter_location(location, df)
    multiples = find_multiples(df)
    df = filter_multiples(df, multiples)
    matches = check_matches(df, multiples)
    consolidations = check_mergable(matches)
    return consolidations