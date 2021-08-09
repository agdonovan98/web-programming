#sets up table with following test data if signed in as "austin"
import dataset

if __name__ == "__main__":
    atlas_list_db = dataset.connect('sqlite:///atlas_list.db')
    place_table = atlas_list_db.get_table('atlas')
    place_table.drop()
    place_table = atlas_list_db.create_table('atlas')
    place_table.insert_many([
        { 'user' : 'austin', 'place' : 'Kent, OH', 'date': 'May 8, 2021', 'comments': 'College'},
        { 'user' : 'austin', 'place' : 'Miami, FL', 'date': 'June 21, 2020', 'comments': 'Vacation'},
        { 'user' : 'austin', 'place' : 'New York City, NY', 'date': 'January 1, 2023', 'comments': 'Hoping to visit!'}        
    ])