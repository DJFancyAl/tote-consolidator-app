import pandas as pd
from locations import locations_870, locations_940
from database_sql import get_inventory

# Variaables
max_weight = 1850 #lbs.

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
        match = match.to_dict(orient="records")
        remaining_totes = match

        for tote in match:
            if tote in remaining_totes:
                for item in remaining_totes:
                    if tote != item:
                        if (tote['weight'] + item['weight']) <= max_weight:
                            consolidations.append([tote, item])
                            remaining_totes.remove(tote)
                            remaining_totes.remove(item)
                            break

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