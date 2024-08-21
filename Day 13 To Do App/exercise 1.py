def fn(st):
    """ Write a get_nr_items function that:

        1. gets as a parameter one string with commas. E.g., "john,lisa, teresa"

        2. the function should return the number of items divided by commas in that string 
           (i.e., that would be three items in the above example)

        2. returns the number of items. """
    cm=0
    for i in st:
        if i == ',':
            cm+=1
    stlist = st.split(',')
    print(len(stlist),cm)

fn("john,lisa, teresa")