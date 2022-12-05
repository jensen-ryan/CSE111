from datetime import datetime
import csv

PRODUCT_NUM_INDEX = 0
def main():
    DISC_RATE = 0.10
    SALES_TAX_RATE = 0.06
    
    print("Inkom Emporium")
    print()
    
    products = read_products()
    
    # Call the process_request function.
    quantity, subtotal = process_request(products)
    print()
    # Calculate and print out the item quantity and total prices.
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    
    # Call the now() method to get the current date and
    # time as a datetime object from the computer's clock.
    current_date_and_time = datetime.now()
    # Format and print the current date and time to include
    # only the day of the week, the hour, and the minute.
    
    # Call the weekday() method to get the day of the
    # week from the current_date_and_time object.
    weekday = current_date_and_time.weekday()
    
    # If today is Tuesday or Wednesday, compute the discount amount.
    if weekday == 1 or weekday == 2:
        discount = round(subtotal * DISC_RATE, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount
        
    # Compute the total by adding the subtotal and the sales tax.
    total = subtotal + sales_tax
    
    # Display the total for the user to see.
    print(f"Total: {total:.2f}")
    
    print(f"Number of Items: {quantity:.0f}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print()
    # Print out concluding thank you message and current time.
    print(f"Thank you for shopping at Inkom Emporium!")
    
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

def read_products():
    products = {}
    # try excepy block in case the file is not found or permission is denied.
    try:
    # Open the products.csv file for reading.
        with open("products.csv", "rt") as products_file:
        # Use a csv.reader to read from the opened file.
            reader = csv.reader(products_file)

            # Skip the first line giving a format.
            next(reader)
            # Define index constants for clarity.

            NAME_INDEX = 1
            PRICE_INDEX = 2
            # Process the file one row at a time.

            for row in reader:
            # Retrieve product information.
                product_num = row[PRODUCT_NUM_INDEX]
                product_name = row[NAME_INDEX]
                product_price = row[PRICE_INDEX]
                # Populate a dictionary with the contents of the products.csv file.
                products[product_num] = [product_name, product_price]

    except FileNotFoundError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"The file products.csv doesn't exist.")
        print("Ensure products.csv exists in the current directory and run theprogram again.")
        exit()

    except PermissionError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"You don't have permission to read products.csv.")
        print("Ensure products.csv grants reading permissions and run theprogramagain.")
        exit()
    except Exception as e:
        print(type(e).__name__, e, sep=": ")
        exit()# Return the dictionary.
    return products

def process_request(products):
    try:
        # Open the request.csv file for reading.
        with open("request.csv", "rt") as requests_file:

            # Use a csv.reader to read from the opened file.
            reader = csv.reader(requests_file)

            # Skip the first line giving a format.
            next(reader)

            QUANTITY_INDEX = 1
            NAME_INDEX = 0
            PRICE_INDEX = 1

            # Process the file one row at a time. Keep tabs on the number
            # of items and the subtotal.
            num_items = 0
            subtotal = 0
            for row in reader:
                product_num = row[PRODUCT_NUM_INDEX]
                product_quantity = int(row[QUANTITY_INDEX])
                num_items += product_quantity
                product = products[product_num]
                product_name = product[NAME_INDEX]
                product_price = float(product[PRICE_INDEX])
                subtotal += product_price * product_quantity

                # Print the product name, requested quantity, and product price.
                print(f"{product_name}: {product_quantity} @ {product_price}")
                print()

    except FileNotFoundError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"The file request.csv doesn't exist.")
        print("Ensure request.csv exists in the current directory and run theprogram again.")
        exit()

    except PermissionError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"You don't have permission to read request.csv.")
        print("Ensure request.csv grants reading permissions and run the programagain.")
        exit()

    except KeyError as e:
        print(type(e).__name__, e, sep=": ")
        print(f"A key requested in request.csv does not exist as an item inproducts.csv.")
        print("Edit products.csv and request.csv files to ensure keys match exactlythen run the program again.")
        exit()

    except Exception as e:
        print(type(e).__name__, e, sep=": ")
        
        return num_items, subtotal

# Call main to start this program.
if __name__ == "__main__":
    main()