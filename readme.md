# API assesment
## Prep
1. The tasks that interact with the Revel API use the Python requests library. 
2. .env contains variables to be used in the API related tasks. The API creds are removed for sharing.
   
## Palindrome finder
Simple as it comes. Input through console.

## Duplicate counter
Looks for input.csv, outputs to console and output.json.

## Most expensive item in order
I assume the bonus points come from simply expanding orders when getting order items. This does not guarantee a single call simply because you cannot filter by dining type that way, and the chance of not hittng an order with the correct dining type is further increased by the fact that you simply will have more orderItems than orders.

This is a long winded way of saying that I found that it would be tedious to actually do it.

## Sorted Menu
Grabs menu, puts it all into a single dict, converts it into a sorted list, prints it.

## Cart Calculate
Does pretty much the same as above - just grabs the first three products in the sorted list and POSTs them to /cart/calculate/