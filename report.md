# AirBnB MongoDB Analysis

## Data Set Details

1. Origin: The data was taken from the Inside Airnb [AirBnB listings data](http://insideairbnb.com/get-the-data.html). I have chosen Nashville, so we have data about all the Airbnb hosts in the Nashville with other information that each of the listings have like utilities, locations, etc, which will be helpful for a customer. The link for Nahville data is [Nashville](http://insideairbnb.com/nashville)
2. The data when downladed was in a .gz format which was later converted into csv.
3. Presenting the data:
   <br>

| id      | listing_url                          | scrape_id   | last_scraped | source      | name                                               | description                                                                                                                                                                    | neighborhood_overview                                                     | picture_url                                                                                            | host_id                                  | host_url                                 | host_name | host_since    | host_location                       | host_about                                                                         | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url                                                                                     | host_picture_url                                                                                            | host_neighbourhood | host_listings_count | host_total_listings_count | host_verifications   | host_has_profile_pic | host_identity_verified | neighbourhood                       | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude | longitude | property_type        | room_type    | accommodates | bathrooms | bathrooms_text | bedrooms | beds | amenities                                                                                                                                                                                                                                                              | price  | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
| ------- | ------------------------------------ | ----------- | ------------ | ----------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------- | ---------------------------------------- | --------- | ------------- | ----------------------------------- | ---------------------------------------------------------------------------------- | ------------------ | ------------------ | -------------------- | ----------------- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- | ------------------ | ------------------- | ------------------------- | -------------------- | -------------------- | ---------------------- | ----------------------------------- | ---------------------- | ---------------------------- | -------- | --------- | -------------------- | ------------ | ------------ | --------- | -------------- | -------- | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------------- | -------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------------- | ---------------- | ---------------- | --------------- | --------------- | --------------- | ---------------- | --------------------- | ----------------- | --------------------- | ---------------------- | ------------ | ----------- | -------------------- | ---------------------- | ------------------------- | --------------------- | --------------------------- | ---------------------- | ------------------- | ------- | ---------------- | ------------------------------ | ------------------------------------------- | -------------------------------------------- | ------------------------------------------- | ----------------- | ---------------------------------- | ----------- | ------- | ----------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------- | ------- | ------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---- | --- | ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- | --- | -------------------- | ----------------------------------- | ----------- | -------- | --------- | ------------------ | --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------ | ------- | ---- | --- | ---- | ---- | ---- | ---- | ---- | --- | ---- | --- |
| 6422    | https://www.airbnb.com/rooms/6422    | 2.02303E+13 | 3/19/23      | city scrape | Nashville Charm                                    | 30 day plus ...d                                                                                                                                                               | Histo...                                                                  | https://...                                                                                            | 12172                                    | https://...                              | Michele   | 4/3/09        | Nashville, TN                       | My husband ... world.                                                              | within an hour     | 100%               | 0%                   | f                 | https://a0.muscache.com/im/users/12172/profile\_pic/1375806408/original.jpg?aki\_policy=profile_small  | https://a0.muscache.com/im/users/12172/profile\_pic/1375806408/original.jpg?aki\_policy=profile\_x\_medium  |                    | 1                   | 1                         | \['phone'\]          | t                    | t                      | Nashville, Tennessee, United States | District 6             |                              | 36.17315 | -86.73581 | Private room in home | Private room | 1            |           | 1 private bath | 1        | 1    | \["Lock on bedroom door", "Iron", "Washer \\u2013\\u00a0In building", "Kayak", "Private living room", "Freezer", "Ethernet connection", "TV", "Mini fridge", "Luggage dropoff allowed", "Bathtub", ..."Heating", "Free driveway parking on premises \\u2013 1 space"\] | $43.00 | 30             | 365            | 30                     | 30                     | 365                    | 365                    | 30                     | 365                    |                  | t                | 0               | 4               | 34              | 309              | 3/19/23               | 674               | 0                     | 0                      | 4/30/09      | 3/3/20      | 4.95                 | 4.94                   | 4.96                      | 4.97                  | 4.96                        | 4.92                   | 4.98                |         | f                | 1                              | 0                                           | 1                                            | 0                                           | 3.99              |
| 39870   | https://www.airbnb.com/rooms/39870   | 2.02303E+13 | 3/19/23      | city scrape | Close to Vanderbilt 2                              | Since I am older, I need for guests to be vaccinated. ...vaccinated.                                                                                                           | The house is in a safe, quiet, "college" neighborhood.                    | https://a0.muscache.com/pictures/miso/Hosting-39870/original/2e51ef52-cb3b-4c2b-9972-8ce50b6acff7.jpeg | 171184                                   | https://www.airbnb.com/users/show/171184 | Evelyn    | 7/18/10       | Nashville, TN                       | I am a newly retired elementary school teacher. I like to run, walk, ... shopping. | within an hour     | 100%               | 92%                  | t                 | https://a0.muscache.com/im/users/171184/profile\_pic/1389073105/original.jpg?aki\_policy=profile_small | https://a0.muscache.com/im/users/171184/profile\_pic/1389073105/original.jpg?aki\_policy=profile\_x\_medium |                    | 1                   | 3                         | \['email', 'phone'\] | t                    | t                      | Nashville, Tennessee, United States | District 18            |                              | 36.12523 | -86.81278 | Private room in home | Private room | 2            |           | 1 private bath | 1        | 1    | \["Iron", "Keypad", "Luggage dropoff allowed", ..., "Carbon monoxide alarm", "Bed linens", "Microwave", "Hangers", "Heating"\]                                                                                                                                         | $70.00 | 1              | 1125           | 1                      | 1                      | 1125                   | 1125                   | 1                      | 1125                   |                  | t                | 5               | 17              | 30              | 174              | 3/19/23               | 349               | 68                    | 1                      | 9/16/16      | 2/26/23     | 4.94                 | 4.96                   | 4.95                      | 4.99                  | 4.97                        | 4.95                   | 4.94                |         | f                | 1                              | 0                                           | 1                                            | 0                                           | 4.41              |
| 3648549 | https://www.airbnb.com/rooms/3648549 | 2.02303E+13 | 3/20/23      | city scrape | Serene, Cozy Getaway; Lipscomb, Vanderbilt,12South | \*Our Airbnb is professionally cleaned & disinfected between each guest’s stay.\* <br> <br>As we say in the South "Y'all come on in, make yourself at home!" <br>... LOCATION, | https://a0.muscache.com/pictures/482b8166-d993-48de-88ab-0f44918b7108.jpg | 931636                                                                                                 | https://www.airbnb.com/users/show/931636 | Debby                                    | 8/6/11    | Nashville, TN | I am an out-going human ...with me? |                                                                                    |                    |                    |                      |                   |                                                                                                        |                                                                                                             |                    |                     |                           |                      |                      |                        |                                     |                        |                              |          |           |                      |              |              |           |                |          |      |                                                                                                                                                                                                                                                                        |        |                |                |                        |                        |                        |                        |                        |                        |                  |                  |                 |                 |                 |                  |                       |                   |                       |                        |              |             |                      |                        |                           |                       |                             |                        |                     |         |                  |                                |                                             |                                              |                                             | 176117            | https://www.airbnb.com/rooms/72906 | 2.02303E+13 | 3/20/23 | city scrape | Vandy/Belmont/10 mins to Broadway - Sunny 800 sqft | Entire top floor. ...Hillsboro Village - 10 minute walk - Fido, J. Pancake Panty, Biscuit Love, Barista Parlor, many great restaurants, funky shops. <br> <br>12 | https://a0.muscache.com/pictures/58602855/37884dd6_original.jpg | https://www.airbnb.com/users/show/176117 | Richard | 7/21/10 | Nashville, TN | I was born in England and came to the US as a young lad. I worked for many years as a professional musician and have composed music for the BBC in London, and written for Network TV. I am a published novelist (STEALING MONA LISA - St. Martin's Press - under the name Carson Morton) and songwriter. I sail, kayak, and love to travel (I'm definitely a Francophile). And now, I can call myself a professional honky tonk dancer, as I've worked as a paid "Honky Tonk Dancer" on the ABC show, "Nashville". I've met some amazing people through airbnb and look forward to meeting more! | within an hour | 100% | t   | https://a0.muscache.com/im/users/176117/profile\_pic/1330356840/original.jpg?aki\_policy=profile_small | https://a0.muscache.com/im/users/176117/profile\_pic/1330356840/original.jpg?aki\_policy=profile\_x\_medium |     | \['email', 'phone'\] | Nashville, Tennessee, United States | District 18 | 36.13122 | -86.80066 | Entire rental unit | Entire home/apt | 1 bath | \["Iron", "Luggage dropoff allowed", "Wifi", "Washer", "Coffee maker", "First aid kit", "Essentials", "... monoxide alarm", "Security cameras on property", "Microwave", "Shared backyard \\u2013 Not fully fenced", "Dishes and silverware", "Hangers", "Heating"\] | $100.00 | 6/9/11 | 3/16/23 | 4.91 | 4.9 | 4.81 | 4.98 | 4.99 | 4.96 | 4.89 | f   | 4.72 |     |
| ---     | ---                                  | ---         | ---          | ---         | ---                                                | ---                                                                                                                                                                            | ---                                                                       | ---                                                                                                    | ---                                      | ---                                      | ---       | ---           | ---                                 | ---                                                                                | ---                | ---                | ---                  | ---               | ---                                                                                                    | ---                                                                                                         | ---                | ---                 | ---                       | ---                  | ---                  | ---                    | ---                                 | ---                    | ---                          | ---      | ---       | ---                  | ---          | ---          | ---       | ---            | ---      | ---  | ---                                                                                                                                                                                                                                                                    | ---    | ---            | ---            | ---                    | ---                    | ---                    | ---                    | ---                    | ---                    | ---              | ---              | ---             | ---             | ---             | ---              | ---                   |

#### The data had a lot of information, therefore I am just showing 3 rows. I used a little assistance of https://www.convertsimple.com/convert-csv-to-markdown-table/.

4. Problems with my data was related to incomplete information. My data had blank/no information for the nrighborhood, which would have latter affected the result in the analysis. I used python to munge by data and get rid of rows with missing neighborhood details. or example in the host_id = 914787, the neighborhood was missing, so while munging it I removed it.

```bash
x = 0
while x < len(information):
    if information[x][13] == "":
        x += 1
        continue
    else:
        new_information.append(information[x])
        x += 1
```

## Analysis

1. The query given below gives us the 2 listings from the listings collection. We are limiting the number which helps us getting only the number of documents we need.
   <br>
   Query:

```bash
db.listings.find().limit(2)
```

Output:

<pre>
[
  {
    _id: ObjectId("643b555124ed49838615859c"),
    id: 39870,
    listing_url: 'https://www.airbnb.com/rooms/39870',
    scrape_id: Long("20230319180930"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'Close to Vanderbilt 2',
    description: 'Since I am ....note</b><br />Since I am older and the room is in my home, I need for guests to be vaccinated.',
    neighborhood_overview: 'The house is in a safe, quiet,  "college" neighborhood.',
    picture_url: 'https://a0.muscache.com/pictures/miso/Hosting-39870/original/2e51ef52-cb3b-4c2b-9972-8ce50b6acff7.jpeg',
    host_id: 171184,
    host_url: 'https://www.airbnb.com/users/show/171184',
    host_name: 'Evelyn',
    host_since: '2010-07-18',
    host_location: 'Nashville, TN',
    host_about: 'I am a newly retired elementary school teacher. I like to run, walk, swim, read and meet new people. I  have three children. The girls are young adults and my son is a freshman away at college. I My cozy home is within walking distance to Vanderbilt and Belmont Universities, restaurants and shopping.',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '92%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/171184/profile_pic/1389073105/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/171184/profile_pic/1389073105/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Nashville, Tennessee, United States',
    neighbourhood_cleansed: 'District 18',
    neighbourhood_group_cleansed: '',
    latitude: 36.12523,
    longitude: -86.81278,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 private bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Iron", "Keypad", "Luggage dropoff allowed", "Free parking on premises", "Wifi", "Washer", "Coffee maker", "Essentials", "Refrigerator", "Self check-in", "Extra pillows and blankets", "Hair dryer", "Shampoo", "Fire extinguisher", "Hot water", "Dryer", "Smoke alarm", "Air conditioning", "Carbon monoxide alarm", "Bed linens", "Microwave", "Hangers", "Heating"]',
    price: '$70.00',
    minimum_nights: 1,
    maximum_nights: 1125,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 1,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 5,
    availability_60: 17,
    availability_90: 30,
    availability_365: 174,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 349,
    number_of_reviews_ltm: 68,
    number_of_reviews_l30d: 1,
    first_review: '2016-09-16',
    last_review: '2023-02-26',
    review_scores_rating: 4.94,
    review_scores_accuracy: 4.96,
    review_scores_cleanliness: 4.95,
    review_scores_checkin: 4.99,
    review_scores_communication: 4.97,
    review_scores_location: 4.95,
    review_scores_value: 4.94,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 4.41
  },
  {
    _id: ObjectId("643b555124ed49838615859b"),
    id: 6422,
    listing_url: 'https://www.airbnb.com/rooms/6422',
    scrape_id: Long("20230319180930"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'Nashville Charm',
    description: "30 day plus rental - book ...Within 15 minutes of most major universities, hospitals, drug and grocery stores and other needed services. East Nashville really does have it all!",
    picture_url: 'https://a0.muscache.com/pictures/miso/Hosting-6422/original/c1ff6506-8d8b-4ccf-927a-0e2275270879.jpeg',
    host_id: 12172,
    host_url: 'https://www.airbnb.com/users/show/12172',
    host_name: 'Michele',
    host_since: '2009-04-03',
    host_location: 'Nashville, TN',
    host_about: "My husband and I are parents of 5 grown children, living in various places in the US attending school/working. We've lived in East Nashville for 20 years. My husband, Collier, is a recently retired public ...all visitors in this world.",
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '0%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/12172/profile_pic/1375806408/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/12172/profile_pic/1375806408/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Nashville, Tennessee, United States',
    neighbourhood_cleansed: 'District 6',
    neighbourhood_group_cleansed: '',
    latitude: 36.17315,
    longitude: -86.73581,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1 private bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Lock on bedroom door", "Iron", "Washer \\u2013\\u00a0In building", "Kayak", "Private living room", "Freezer", "Ethernet connection", "TV", "Mini fridge", "Luggage dropoff allowed", "Bathtub", "Wifi", "Ceiling fan", "Essentials", "First aid kit", "Cooking basics", "Extra pillows and blankets", "Hair dryer", "Shampoo", "Books and reading material", "Dedicated workspace", "Hammock", "Shared patio or balcony", "Toaster", "Dr. Bronners body soap", "Cleaning products", "All natural conditioner", "Fire extinguisher", "Hot water", "Backyard", "Free street parking", "Coffee maker: pour-over coffee", "Smoke alarm", "Air conditioning", "Outdoor dining area", "Carbon monoxide alarm", "Hot water kettle", "Bed linens", "Clothing storage: closet, wardrobe, and dresser", "Coffee", "Long term stays allowed", "Microwave", "Portable fans", "Kitchen", "Hangers", "Dishes and silverware", "Room-darkening shades", "Outdoor furniture", "Dryer \\u2013 In building", "Host greets you", "Heating", "Free driveway parking on premises \\u2013 1 space"]',
    price: '$43.00',
    minimum_nights: 30,
    maximum_nights: 365,
    minimum_minimum_nights: 30,
    maximum_minimum_nights: 30,
    minimum_maximum_nights: 365,
    maximum_maximum_nights: 365,
    minimum_nights_avg_ntm: 30,
    maximum_nights_avg_ntm: 365,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 0,
    availability_60: 4,
    availability_90: 34,
    availability_365: 309,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 674,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2009-04-30',
    last_review: '2020-03-03',
    review_scores_rating: 4.95,
    review_scores_accuracy: 4.94,
    review_scores_cleanliness: 4.96,
    review_scores_checkin: 4.97,
    review_scores_communication: 4.96,
    review_scores_location: 4.92,
    review_scores_value: 4.98,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 3.99
  }
]
</pre>

2. In this query we are using the pretty() function. This helpes in putting the data/document in a way that is easy and convenient to read.
   <br>

Query:

```bash
db.listings.find().limit(10).pretty()
```

I did put the ouput for 3 documents because each documnet had a lot of information. Putting 10 increased the output greatly.

```bash
db.listings.find().limit(3).pretty()
```

Output:

<pre>
[
  {
    _id: ObjectId("643b555124ed49838615859c"),
    id: 39870,
    listing_url: 'https://www.airbnb.com/rooms/39870',
    scrape_id: Long("20230319180930"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'Close to Vanderbilt 2',
    description: 'Since I am older, I need for guests to be vaccinated.<br />This is a room and ...Other things to note</b><br />Since I am older and the room is in my home, I need for guests to be vaccinated.',
    neighborhood_overview: 'The house is in a safe, quiet,  "college" neighborhood.',
    picture_url: 'https://a0.muscache.com/pictures/miso/Hosting-39870/original/2e51ef52-cb3b-4c2b-9972-8ce50b6acff7.jpeg',
    host_id: 171184,
    host_url: 'https://www.airbnb.com/users/show/171184',
    host_name: 'Evelyn',
    host_since: '2010-07-18',
    host_location: 'Nashville, TN',
    host_about: 'I am a newly retired elementary school teacher. I like to run, walk, swim, read and meet new people. I  have three children. The girls are young adults and my son is a freshman away at college. I My cozy home is within walking distance to Vanderbilt and Belmont Universities, restaurants and shopping.',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '92%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/171184/profile_pic/1389073105/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/171184/profile_pic/1389073105/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Nashville, Tennessee, United States',
    neighbourhood_cleansed: 'District 18',
    neighbourhood_group_cleansed: '',
    latitude: 36.12523,
    longitude: -86.81278,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 private bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Iron", "Keypad", "Luggage dropoff allowed", "Free parking on premises", "Wifi", "Washer", "Coffee maker", "Essentials", "Refrigerator", "Self check-in", "Extra pillows and blankets", "Hair dryer", "Shampoo", "Fire extinguisher", "Hot water", "Dryer", "Smoke alarm", "Air conditioning", "Carbon monoxide alarm", "Bed linens", "Microwave", "Hangers", "Heating"]',
    price: '$70.00',
    minimum_nights: 1,
    maximum_nights: 1125,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 1,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 5,
    availability_60: 17,
    availability_90: 30,
    availability_365: 174,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 349,
    number_of_reviews_ltm: 68,
    number_of_reviews_l30d: 1,
    first_review: '2016-09-16',
    last_review: '2023-02-26',
    review_scores_rating: 4.94,
    review_scores_accuracy: 4.96,
    review_scores_cleanliness: 4.95,
    review_scores_checkin: 4.99,
    review_scores_communication: 4.97,
    review_scores_location: 4.95,
    review_scores_value: 4.94,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 4.41
  },
  {
    _id: ObjectId("643b555124ed49838615859b"),
    id: 6422,
    listing_url: 'https://www.airbnb.com/rooms/6422',
    scrape_id: Long("20230319180930"),
    last_scraped: '2023-03-19',
    source: 'city scrape',
    name: 'Nashville Charm',
    description: "30 day plus rental - book for one month and then discuss longer rental option. Turn ...the lower Broadway honkey-tonks while others enjoy the local eateries and small music venues throughout our Little-Five Points neighborhood. Within 15 minutes of most major universities, hospitals, drug and grocery stores and other needed services. East Nashville really does have it all!",
    picture_url: 'https://a0.muscache.com/pictures/miso/Hosting-6422/original/c1ff6506-8d8b-4ccf-927a-0e2275270879.jpeg',
    host_id: 12172,
    host_url: 'https://www.airbnb.com/users/show/12172',
    host_name: 'Michele',
    host_since: '2009-04-03',
    host_location: 'Nashville, TN',
    host_about: "My husband and I are parents of 5 grown children, living in various places in the US ...believe in radical hospitality because we are all visitors in this world.",
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '0%',
    host_is_superhost: 'f',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/12172/profile_pic/1375806408/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/12172/profile_pic/1375806408/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Nashville, Tennessee, United States',
    neighbourhood_cleansed: 'District 6',
    neighbourhood_group_cleansed: '',
    latitude: 36.17315,
    longitude: -86.73581,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1 private bath',
    bedrooms: 1,
    beds: 1,
    amenities: '["Lock on bedroom door", "Iron", "Washer \\u2013\\u00a0In building", "Kayak", "Private living room", "Freezer", "Ethernet connection", "TV", "Mini fridge", "Luggage dropoff allowed", "Bathtub", "Wifi", "Ceiling fan", "Essentials", "First aid kit", "Cooking basics", "Extra pillows and blankets", "Hair dryer", "Shampoo", "Books and reading material", "Dedicated workspace", "Hammock", "Shared patio or balcony", "Toaster", "Dr. Bronners body soap", "Cleaning products", "All natural conditioner", "Fire extinguisher", "Hot water", "Backyard", "Free street parking", "Coffee maker: pour-over coffee", "Smoke alarm", "Air conditioning", "Outdoor dining area", "Carbon monoxide alarm", "Hot water kettle", "Bed linens", "Clothing storage: closet, wardrobe, and dresser", "Coffee", "Long term stays allowed", "Microwave", "Portable fans", "Kitchen", "Hangers", "Dishes and silverware", "Room-darkening shades", "Outdoor furniture", "Dryer \\u2013 In building", "Host greets you", "Heating", "Free driveway parking on premises \\u2013 1 space"]',
    price: '$43.00',
    minimum_nights: 30,
    maximum_nights: 365,
    minimum_minimum_nights: 30,
    maximum_minimum_nights: 30,
    minimum_maximum_nights: 365,
    maximum_maximum_nights: 365,
    minimum_nights_avg_ntm: 30,
    maximum_nights_avg_ntm: 365,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 0,
    availability_60: 4,
    availability_90: 34,
    availability_365: 309,
    calendar_last_scraped: '2023-03-19',
    number_of_reviews: 674,
    number_of_reviews_ltm: 0,
    number_of_reviews_l30d: 0,
    first_review: '2009-04-30',
    last_review: '2020-03-03',
    review_scores_rating: 4.95,
    review_scores_accuracy: 4.94,
    review_scores_cleanliness: 4.96,
    review_scores_checkin: 4.97,
    review_scores_communication: 4.96,
    review_scores_location: 4.92,
    review_scores_value: 4.98,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 3.99
  },{
    _id: ObjectId("643b555124ed49838615859d"),
    id: 3648549,
    listing_url: 'https://www.airbnb.com/rooms/3648549',
    scrape_id: Long("20230319180930"),
    last_scraped: '2023-03-20',
    source: 'city scrape',
    name: 'Serene, Cozy Getaway; Lipscomb, Vanderbilt,12South',
    description: `*Our Airbnb is professionally cleaned & disinfected between each guest’s stay.*<br /><br />As we say in the South "Y'all come on in, make yourself at home!"<br />Create great ...track right beside our house on Lipscomb's High School athletic field that is available for your free use. <br /><br />LOCATION, LOCATION, ",
    picture_url: 'https://a0.muscache.com/pictures/482b8166-d993-48de-88ab-0f44918b7108.jpg',
    host_id: 931636,
    host_url: 'https://www.airbnb.com/users/show/931636',
    host_name: 'Debby',
    host_since: '2011-08-06',
    host_location: 'Nashville, TN',
    host_about: "I am an out-going human being who believes that what I give out to the world comes ...wind, rain, snow, sleet, and whatever came our way and BOY what great memories!",
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 't',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/1bf9abec-c6db-44f9-a8f4-edaeab17655f.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/1bf9abec-c6db-44f9-a8f4-edaeab17655f.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 't',
    host_identity_verified: 't',
    neighbourhood: 'Nashville, Tennessee, United States',
    neighbourhood_cleansed: 'District 25',
    neighbourhood_group_cleansed: '',
    latitude: 36.10373,
    longitude: -86.79625,
    property_type: 'Entire rental unit',
    room_type: 'Entire home/apt',
    accommodates: 4,
    bathrooms: '',
    bathrooms_text: '1 bath',
    bedrooms: 1,
    beds: 3,
    amenities: '["Wine glasses", "Iron", "Body soap", "Private entrance", "Keypad", "Luggage dropoff allowed", "Free parking on premises", "Wifi", "Washer", "Coffee maker", "Ceiling fan", "Essentials", "First aid kit", "Refrigerator", "Self check-in", "Extra pillows and blankets", "Clothing storage: closet and dresser", "TV with standard cable", "Single level home", "Hair dryer", "Shampoo", "Books and reading material", "Backyard", "Toaster", "Fire extinguisher", "Hot water", "Dryer", "Safe", "Smoke alarm", "Air conditioning", "Carbon monoxide alarm", "Bed linens", "Patio or balcony", "Long term stays allowed", "Microwave", "Dishes and silverware", "Hangers", "Dining table", "Heating"]',
    price: '$143.00',
    minimum_nights: 2,
    maximum_nights: 34,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 1.7,
    maximum_nights_avg_ntm: 1125,
    calendar_updated: '',
    has_availability: 't',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    calendar_last_scraped: '2023-03-20',
    number_of_reviews: 141,
    number_of_reviews_ltm: 25,
    number_of_reviews_l30d: 0,
    first_review: '2016-10-23',
    last_review: '2022-11-14',
    review_scores_rating: 4.93,
    review_scores_accuracy: 4.95,
    review_scores_cleanliness: 4.91,
    review_scores_checkin: 4.97,
    review_scores_communication: 4.97,
    review_scores_location: 4.94,
    review_scores_value: 4.93,
    license: '',
    instant_bookable: 'f',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 1,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 1.81
  }
]
- Here I used the limit 3 because the document had a lot of columns that made the output very large.
</pre>

3. This query is only getting us the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result(superhost). We are limiting our result to the coulmns which we need.

Query:

```bash
db.listings.find({
    $and: [
  {host_id: { $in: [ 171184, 931636 ] }}]
}, {
  name: 1,
  price: 1,
  neighbourhood: 1,
  host_name: 1,
  host_is_superhost: 1,
  _id: 0
})
```

Output:

<pre>
[
  {
    name: 'Close to Vanderbilt 2',
    host_name: 'Evelyn',
    host_is_superhost: 't',
    neighbourhood: 'Nashville, Tennessee, United States',
    price: '$70.00'
  },
  {
    name: 'Serene, Cozy Getaway; Lipscomb, Vanderbilt,12South',
    host_name: 'Debby',
    host_is_superhost: 't',
    neighbourhood: 'Nashville, Tennessee, United States',
    price: '$143.00'
  },
  {
    name: 'Close to Vanderbilt 2',
    host_name: 'Evelyn',
    host_is_superhost: 't',
    neighbourhood: 'Nashville, Tennessee, United States',
    price: '$70.00'
  }
]
</pre>

4. This query helps us get the total number of host, which will be impossible to get if we try doing it mechanically. We will be getting all the distinct hosts.

Query:

```bash
db.listings.distinct("host_name")
```

Output:

<pre>
[
  NaN,                    '12th',                '12th South',
  'A.',                   'Aaron',               'Abbie And Corbin',
  'Abby',                 'Abdullatif',          'Abey',
  'Abigail',              'Abigail And Kyle',    'Abode (Nashville)',
  'Above Vacation',       'Abraham',             "Ad'Breona",
  'Adam',                 'Adam And Tia',        'Addison',
  'Adi',                  'Aditi',               'Adrian',
  'Adrienne',             'Agnes',               'Ahmet',
  'Aidan',                'Aide',                'Aieshia',
  'Aimee & Chris',        'Aj',                  'Ajay',
  'Akilah',               'Alaina',              'Alan',
  'Alana',                'Alayna',              'Albert',
  'Alberto',              'Albis Junior',        'Albron',
  'Alec',                 'Alece',               'Alectra',
  'Alena',                'Alex',                'Alex & Wes',
  'Alex From Abode',      'Alexa',               'Alexa & Emily',
  'Alexander',            'Alexanderia',         'Alexandra',
  'Alexandria',           'Alexis',              'Alexis N',
  'Ali',                  'Alianna & Kenneth',   'Alicia',
  'Alisa',                'Alison',              'Alissa',
  'All Around Knowledge', 'All En Stays',        'Allan',
  'Allen',                'Allen And  Jennifer', 'Alli',
  'Allie',                'Allin',               'Allison',
  'Allyson',              'Alphonse',            'Alphonso',
  'Alta',                 'Alvin',               'Aly',
  'Alynn',                'Alysha',              'Alyssa',
  'Alyssa & Konrad',      'Amanda',              'Amani',
  'Amarilis',             'Amber',               'Amber & Brett',
  'Amber & Jordan',       'Ambra',               'Amelia',
  'Amesia',               'Amory',               'Amy',
  'Amy & Brandon',        'Amy & Jarrod',        'Anastasia',
  'Anchor Rentals',       'Andi',                'Andi Jane',
  'Andrea',               'Andrew',              'Andrew & Lisa',
  'Andrew & Rachel',
  ... 1505 more items
]
</pre>

5. This query gives us the `name`, `beds`, `review_scores_rating`, and `price` of the places that have more than 2 `beds` in a neighborhood, Nashville, Tennessee, United States. We use the operator $gt and we get our result.

Query:

```bash
db.listings.find(
  {
    $and: [
    { neighbourhood: "Nashville, Tennessee, United States" },
    {beds: { $gt: 2 }}]
  },
  {
    name: 1,
    beds: 1,
    review_scores_rating: 1,
    price: 1,
    _id: 0
  }
).sort({ "review_scores_rating": -1 })
```

</pre>
Output:
<pre>
[
  {
    name: 'CONDO IN THE HEART OF GREEN HILLS',
    beds: 4,
    price: '$700.00',
    review_scores_rating: ''
  },
  {
    name: 'Tyler House at East Nashville',
    beds: 4,
    price: '$357.00',
    review_scores_rating: ''
  },
  {
    name: 'East Nash Boho Bungalow',
    beds: 7,
    price: '$189.00',
    review_scores_rating: ''
  }
]
</pre>

6. Here we wanted to get the number of listings per host. So we are grouping by the host_id and they counting the listings. We are

Query:

```bash
db.listings.aggregate([
  { $group: { _id: "$host_id", count: { $sum: 1 } } }
])
```

Output:

<pre>
[] { _id: 75621208, count: 1 },
  { _id: 355260892, count: 1 },
  { _id: 31778647, count: 1 }
  ]
</pre>

If we put the sorting function to get the host with the most number of listings.<br>
Query:

```bash
db.listings.aggregate([
  { $group: { _id: "$host_id", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])
```

Output:

<pre>
[
  { _id: 101426897, count: 185 },
  { _id: 20772148, count: 173 },
  { _id: 134126657, count: 151 }
]
</pre>

7.  Here we are get the average rating according to each of the neighborhood. I do not have any empty neighborhood because I munged the rows which no information about the neighborhood. We are only showing the neighborhood that has avergae rating of 95%5, since all the ratings are out of 5.
    <br>

Query:

```bash
    db.listings.aggregate([
  { $match: { review_scores_rating: { $gt: 95%5 } } },
  { $group: { _id: "$neighbourhood", average_rating: { $avg: "$review_scores_rating" } } },
  { $sort: { average_rating: -1 } }
])
```

- I am sorting here according to the average rating and because in my data set the rating were given out of 5, I am printing data that has rating avove 95% of 5.

Output:

<pre>
[
  { _id: 'Ashland City, Tennessee, United States', average_rating: 5 },
  { _id: 'NASHVILLE, Tennessee, United States', average_rating: 5 },
  {
    _id: 'Nashville Hermitage, Tennessee, United States',
    average_rating: 5
  }
]
</pre>

#### Describe any insights the analysis shows that may not be obvious to someone just viewing the raw data:

In the data we used function like aggregate, distinct, avergae and then we also used group by for on of the quet. This helps in calculating data with a very large data with no fixed schema, quickly and efficiently. The best thing about using mongoDb is that we do not need a fixed schema, we can work without it with functions like aggregate, average, etc.
