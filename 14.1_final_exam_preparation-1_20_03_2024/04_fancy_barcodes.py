import re


def parse_barcode(barcode_data):
    pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

    for barcode in barcode_data:
        match = re.fullmatch(pattern, barcode)

        if match:
            product_group = ''.join(re.findall('\d', barcode))

            if product_group:
                product_group = product_group
            else:
                product_group = "00"
            print(f"Product group: {product_group}")
        else:
            print("Invalid barcode")


count_barcodes = int(input())
data = [input() for barcode in range(count_barcodes)]

parse_barcode(data)
