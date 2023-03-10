# Tweaked slightly from here: https://github.com/datamade/usaddress/issues/105
# After running this once, it'll be easier to find what needs to be cleaned up for a second run or before cleansing/geocoding

import csvkit
import usaddress

# https://docs.python.org/3.5/library/functions.html#open
with open(r"C:\Users\JohnsonN35\project_path\addr.csv", 'r') as f:
    reader = csvkit.DictReader(f)

    all_rows = []
    for row in reader:
        try:
            tagged_addr = usaddress.tag(row['Address_Full']) # Tag function is better than parse function at keeping e.g. "Benton Harbor" as one place name 
            row_dict = tagged_addr[0]
        except:
            row_dict = {'error':'True'}

        row_dict['Input_JoinID'] = row['Input_JoinID']  # Field in original data that you want to keep
        row_dict['Address_Full'] = row['Address_Full']  # "
        row_dict['Address_Original'] = row['Address_Original']  # "
        all_rows.append(row_dict)

# Besides the fields in the original data, want to include all of the possible keys in usaddress (most records won't have any data for most of these fields)
field_list = ['Input_JoinID', 'Address_Full', 'Address_Original', 'AddressNumber', 'AddressNumberPrefix', 'AddressNumberSuffix', 'BuildingName', 
              'CornerOf','IntersectionSeparator','LandmarkName','NotAddress','OccupancyType', 'OccupancyIdentifier','PlaceName','Recipient','StateName','StreetName',
              'StreetNamePreDirectional','StreetNamePreModifier','StreetNamePreType', 'StreetNamePostDirectional','StreetNamePostModifier','StreetNamePostType',
              'SubaddressIdentifier','SubaddressType','USPSBoxGroupID','USPSBoxGroupType', 'USPSBoxID','USPSBoxType','ZipCode', 'error']

with open(r"C:\Users\JohnsonN35\project_path\addr_tagged.csv", 'w') as outfile:
    writer = csvkit.DictWriter(outfile, field_list)
    writer.writeheader()
    writer.writerows(all_rows)
