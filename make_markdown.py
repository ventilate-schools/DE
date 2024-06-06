import os
import pandas as pd

schools = {
    "Appoquinimink School District": [
        {
            "school_name": "Appoquinimink High School",
            "address": "1080 Bunker Hill Rd, Middletown, DE 19709",
            "phone": "302-449-3840",
            "website": "https://www.appohigh.org",
            "students": 1600,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Middletown High School",
            "address": "120 Silver Lake Rd, Middletown, DE 19709",
            "phone": "302-376-4141",
            "website": "https://www.middletownhs.org",
            "students": 1500,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Odessa High School",
            "address": "570 Tony Marchio Dr, Townsend, DE 19734",
            "phone": "302-842-2625",
            "website": "https://www.odessahs.org",
            "students": 1400,
            "grade_levels": "9-12"
        }
    ],
    "Brandywine School District": [
        {
            "school_name": "Brandywine High School",
            "address": "1400 Foulk Rd, Wilmington, DE 19803",
            "phone": "302-479-1600",
            "website": "https://www.brandywineschools.org/brandywine",
            "students": 1000,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Concord High School",
            "address": "2501 Ebright Rd, Wilmington, DE 19810",
            "phone": "302-475-3951",
            "website": "https://www.brandywineschools.org/concord",
            "students": 1200,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Mount Pleasant High School",
            "address": "5201 Washington St Extension, Wilmington, DE 19809",
            "phone": "302-762-7125",
            "website": "https://www.brandywineschools.org/mount",
            "students": 1100,
            "grade_levels": "9-12"
        },
        {
            "school_name": "P.S. duPont Middle School",
            "address": "701 W 34th St, Wilmington, DE 19802",
            "phone": "302-762-7146",
            "website": "https://www.brandywineschools.org/psdupont",
            "students": 800,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Springer Middle School",
            "address": "2220 Shipley Rd, Wilmington, DE 19803",
            "phone": "302-479-1621",
            "website": "https://www.brandywineschools.org/springer",
            "students": 850,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Talley Middle School",
            "address": "1110 Cypress Rd, Wilmington, DE 19810",
            "phone": "302-475-3976",
            "website": "https://www.brandywineschools.org/talley",
            "students": 900,
            "grade_levels": "6-8"
        },
        {
            "school_name": "David W. Harlan Elementary School",
            "address": "3601 N Jefferson St, Wilmington, DE 19802",
            "phone": "302-762-7156",
            "website": "https://www.brandywineschools.org/harlan",
            "students": 400,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Carrcroft Elementary School",
            "address": "503 Crest Rd, Wilmington, DE 19803",
            "phone": "302-762-7165",
            "website": "https://www.brandywineschools.org/carrcroft",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Claymont Elementary School",
            "address": "3401 Green St, Claymont, DE 19703",
            "phone": "302-792-3880",
            "website": "https://www.brandywineschools.org/claymont",
            "students": 500,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Forwood Elementary School",
            "address": "1900 Westminster Dr, Wilmington, DE 19810",
            "phone": "302-475-3956",
            "website": "https://www.brandywineschools.org/forwood",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Hanby Elementary School",
            "address": "2523 Berwyn Rd, Wilmington, DE 19810",
            "phone": "302-479-2220",
            "website": "https://www.brandywineschools.org/hanby",
            "students": 400,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Harlan Elementary School",
            "address": "3601 N Jefferson St, Wilmington, DE 19802",
            "phone": "302-762-7156",
            "website": "https://www.brandywineschools.org/harlan",
            "students": 300,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Lancashire Elementary School",
            "address": "2000 Naamans Rd, Wilmington, DE 19810",
            "phone": "302-475-3990",
            "website": "https://www.brandywineschools.org/lancashire",
            "students": 400,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Lombardy Elementary School",
            "address": "412 Foulk Rd, Wilmington, DE 19803",
            "phone": "302-762-7190",
            "website": "https://www.brandywineschools.org/lombardy",
            "students": 350,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Maple Lane Elementary School",
            "address": "100 Maple Rd, Claymont, DE 19703",
            "phone": "302-792-3906",
            "website": "https://www.brandywineschools.org/maple",
            "students": 300,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Mount Pleasant Elementary School",
            "address": "500 Duncan Rd, Wilmington, DE 19809",
            "phone": "302-762-7120",
            "website": "https://www.brandywineschools.org/mountpleasantelementary",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Charles W. Bush Early Education Center",
            "address": "910 N Orange St, Wilmington, DE 19801",
            "phone": "302-429-4136",
            "website": "https://www.brandywineschools.org/bush",
            "students": 200,
            "grade_levels": "PreK"
        },
        {
            "school_name": "Joseph Brumskill Early Childhood Assistance Program (ECAP)",
            "address": "701 W 34th St, Wilmington, DE 19802",
            "phone": "302-762-7186",
            "website": "https://www.brandywineschools.org/brumskill",
            "students": 150,
            "grade_levels": "PreK"
        }
    ],
    "Caesar Rodney School District": [
        {
            "school_name": "Caesar Rodney High School",
            "address": "239 Old North Rd, Camden, DE 19934",
            "phone": "302-697-2161",
            "website": "https://www.crk12.org/crhs",
            "students": 2100,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Dover Air Base Middle School",
            "address": "3100 Hawthorne Dr, Dover, DE 19901",
            "phone": "302-674-3284",
            "website": "https://www.crk12.org/dabm",
            "students": 600,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Fred Fifer III Middle School",
            "address": "109 E Camden Wyoming Ave, Camden, DE 19934",
            "phone": "302-698-8400",
            "website": "https://www.crk12.org/fifer",
            "students": 650,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Magnolia Middle School",
            "address": "249 W Walnut St, Magnolia, DE 19962",
            "phone": "302-335-5039",
            "website": "https://www.crk12.org/magnolia",
            "students": 700,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Postlethwait (F. Niel) Middle School",
            "address": "2841 S State St, Camden, DE 19934",
            "phone": "302-698-8410",
            "website": "https://www.crk12.org/postlethwait",
            "students": 900,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Frear (Allen) Elementary School",
            "address": "238 Sorghum Mill Rd, Camden, DE 19934",
            "phone": "302-697-3279",
            "website": "https://www.crk12.org/frear",
            "students": 500,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Robinson (David E.) Elementary School",
            "address": "14 Old North Rd, Dover, DE 19901",
            "phone": "302-698-4230",
            "website": "https://www.crk12.org/robinson",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Simpson (W.B.) Elementary School",
            "address": "5 Old North Rd, Camden, DE 19934",
            "phone": "302-697-3207",
            "website": "https://www.crk12.org/simpson",
            "students": 480,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Star Hill Elementary School",
            "address": "594 Voshells Mill Star Hill Rd, Dover, DE 19901",
            "phone": "302-697-6117",
            "website": "https://www.crk12.org/starhill",
            "students": 470,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Stokes (Nellie H.) Elementary School",
            "address": "3874 Upper King Rd, Dover, DE 19904",
            "phone": "302-697-3205",
            "website": "https://www.crk12.org/stokes",
            "students": 460,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Welch (George) Elementary School",
            "address": "3100 Hawthorne Dr, Dover, DE 19901",
            "phone": "302-674-9080",
            "website": "https://www.crk12.org/welch",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "McIlvaine Early Childhood Center",
            "address": "11 E Walnut St, Magnolia, DE 19962",
            "phone": "302-335-5039",
            "website": "https://www.crk12.org/mcilvaine",
            "students": 300,
            "grade_levels": "PreK"
        },
        {
            "school_name": "Caesar Rodney Early Intervention Program",
            "address": "1392 Forrest Ave, Dover, DE 19904",
            "phone": "302-697-2170",
            "website": "https://www.crk12.org/earlyintervention",
            "students": 100,
            "grade_levels": "Special Needs"
        }
    ],
    "Cape Henlopen School District": [
        {
            "school_name": "Cape Henlopen High School",
            "address": "1250 Kings Hwy, Lewes, DE 19958",
            "phone": "302-645-7711",
            "website": "https://www.capehenlopenschools.com/capehenlopen",
            "students": 1500,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Beacon Middle School",
            "address": "19483 John J Williams Hwy, Lewes, DE 19958",
            "phone": "302-645-6288",
            "website": "https://www.capehenlopenschools.com/beacon",
            "students": 800,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Mariner Middle School",
            "address": "16391 Harbeson Rd, Milton, DE 19968",
            "phone": "302-684-8516",
            "website": "https://www.capehenlopenschools.com/mariner",
            "students": 700,
            "grade_levels": "6-8"
        },
        {
            "school_name": "New Middle School (planned)",
            "address": "Lewes, DE",
            "phone": "N/A",
            "website": "N/A",
            "students": 500,
            "grade_levels": "6-8",
            "opening_date": "2024"
        },
        {
            "school_name": "Brittingham (H.O.) Elementary School",
            "address": "400 Mulberry St, Milton, DE 19968",
            "phone": "302-684-8522",
            "website": "https://www.capehenlopenschools.com/brittingham",
            "students": 550,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Love Creek Elementary School",
            "address": "19488 John J Williams Hwy, Lewes, DE 19958",
            "phone": "302-703-3456",
            "website": "https://www.capehenlopenschools.com/lovecreek",
            "students": 600,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Milton Elementary School",
            "address": "512 Federal St, Milton, DE 19968",
            "phone": "302-684-2516",
            "website": "https://www.capehenlopenschools.com/milton",
            "students": 500,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Rehoboth Elementary School",
            "address": "500 Stockley St, Rehoboth Beach, DE 19971",
            "phone": "302-227-4599",
            "website": "https://www.capehenlopenschools.com/rehoboth",
            "students": 550,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Shields (Richard A.) Elementary School",
            "address": "910 Shields Ave, Lewes, DE 19958",
            "phone": "302-645-7748",
            "website": "https://www.capehenlopenschools.com/shields",
            "students": 650,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Sussex Consortium",
            "address": "17344 Sweetbriar Rd, Lewes, DE 19958",
            "phone": "302-644-1446",
            "website": "https://www.capehenlopenschools.com/sussexconsortium",
            "students": 400,
            "grade_levels": "PreK-12"
        },
        {
            "school_name": "McIlvaine Early Childhood Center",
            "address": "11 E Walnut St, Magnolia, DE 19962",
            "phone": "302-335-5039",
            "website": "https://www.capehenlopenschools.com/mcilvaine",
            "students": 300,
            "grade_levels": "PreK"
        },
        {
            "school_name": "Caesar Rodney Early Intervention Program",
            "address": "1392 Forrest Ave, Dover, DE 19904",
            "phone": "302-697-2170",
            "website": "https://www.capehenlopenschools.com/earlyintervention",
            "students": 100,
            "grade_levels": "Special Needs"
        }
    ],
    "Capital School District": [
        {
            "school_name": "Dover High School",
            "address": "1 Dover High Dr, Dover, DE 19904",
            "phone": "302-241-2400",
            "website": "https://www.capital.k12.de.us/dover",
            "students": 1800
        },
        {
            "school_name": "Central Middle School",
            "address": "211 Delaware Ave, Dover, DE 19901",
            "phone": "302-672-1772",
            "website": "https://www.capital.k12.de.us/central",
            "students": 900
        }
    ],
    "Christina School District": [
        {
            "school_name": "Newark High School",
            "address": "750 E Delaware Ave, Newark, DE 19711",
            "phone": "302-631-4700",
            "website": "https://www.christinak12.org/newark",
            "students": 1500
        },
        {
            "school_name": "Christiana High School",
            "address": "190 Salem Church Rd, Newark, DE 19713",
            "phone": "302-631-2400",
            "website": "https://www.christinak12.org/christiana",
            "students": 1200
        }
    ],
    "Colonial School District": [
        {
            "school_name": "William Penn High School",
            "address": "713 E Basin Rd, New Castle, DE 19720",
            "phone": "302-323-2800",
            "website": "https://www.colonialschooldistrict.org/williampenn",
            "students": 2000
        },
        {
            "school_name": "Calvin R. McCullough Middle School",
            "address": "20 Chase Avenue, New Castle, DE 19720",
            "phone": "302-429-4000",
            "website": "https://www.colonialschooldistrict.org/mccullough",
            "students": 800
        },
        {
            "school_name": "George Read Middle School",
            "address": "314 E Basin Rd, New Castle, DE 19720",
            "phone": "302-323-2760",
            "website": "https://www.colonialschooldistrict.org/georgeread",
            "students": 850
        },
        {
            "school_name": "Gunning Bedford Middle School",
            "address": "801 Cox Neck Rd, New Castle, DE 19720",
            "phone": "302-832-6280",
            "website": "https://www.colonialschooldistrict.org/gunningbedford",
            "students": 900
        },
        {
            "school_name": "Castle Hills Elementary School",
            "address": "502 Moores Ln, New Castle, DE 19720",
            "phone": "302-323-2915",
            "website": "https://www.colonialschooldistrict.org/castle-hills",
            "students": 600
        },
        {
            "school_name": "Carrie Downie Elementary School",
            "address": "1201 Delaware St, New Castle, DE 19720",
            "phone": "302-323-2926",
            "website": "https://www.colonialschooldistrict.org/carrie-downie",
            "students": 500
        },
        {
            "school_name": "Colwyck Elementary School",
            "address": "12 Landers Ln, New Castle, DE 19720",
            "phone": "302-429-4000",
            "website": "https://www.colonialschooldistrict.org/colwyck",
            "students": 450
        },
        {
            "school_name": "Harry O. Eisenberg Elementary School",
            "address": "27 Landers Ln, New Castle, DE 19720",
            "phone": "302-429-4000",
            "website": "https://www.colonialschooldistrict.org/eisenberg",
            "students": 550
        },
        {
            "school_name": "New Castle Elementary School",
            "address": "903 Delaware St, New Castle, DE 19720",
            "phone": "302-323-2880",
            "website": "https://www.colonialschooldistrict.org/new-castle",
            "students": 500
        },
        {
            "school_name": "Pleasantville Elementary School",
            "address": "16 Pleasant Place, New Castle, DE 19720",
            "phone": "302-429-4085",
            "website": "https://www.colonialschooldistrict.org/pleasantville",
            "students": 600
        },
        {
            "school_name": "Southern Elementary School",
            "address": "795 Cox Neck Rd, New Castle, DE 19720",
            "phone": "302-832-6300",
            "website": "https://www.colonialschooldistrict.org/southern",
            "students": 700
        },
        {
            "school_name": "Wilmington Manor Elementary School",
            "address": "200 E Roosevelt Ave, New Castle, DE 19720",
            "phone": "302-323-2929",
            "website": "https://www.colonialschooldistrict.org/wilmington-manor",
            "students": 450
        },
        {
            "school_name": "Kathleen H. Wilbur Elementary School",
            "address": "4050 Wrangle Hill Rd, Bear, DE 19701",
            "phone": "302-832-6330",
            "website": "https://www.colonialschooldistrict.org/wilbur",
            "students": 650
        }
    ],
"Delmar School District": [
        {
            "school_name": "Delmar High School",
            "address": "200 N Eighth St, Delmar, DE 19940",
            "phone": "302-846-9544",
            "website": "https://www.delmar.k12.de.us",
            "students": 700
        },
        {
            "school_name": "Delmar Middle School",
            "address": "200 N Eighth St, Delmar, DE 19940",
            "phone": "302-846-9544",
            "website": "https://www.delmar.k12.de.us",
            "students": 600
        }
    ],
    "Indian River School District": [
        {
            "school_name": "Indian River High School",
            "address": "29772 Armory Rd, Dagsboro, DE 19939",
            "phone": "302-732-1500",
            "website": "https://www.irsd.net",
            "students": 900
        },
        {
            "school_name": "Sussex Central High School",
            "address": "26026 Patriots Way, Georgetown, DE 19947",
            "phone": "302-934-3166",
            "website": "https://www.irsd.net",
            "students": 1300
        },
        {
            "school_name": "Georgetown Middle School",
            "address": "301 W Market St, Georgetown, DE 19947",
            "phone": "302-856-1900",
            "website": "https://www.irsd.net",
            "students": 700
        },
        {
            "school_name": "Millsboro Middle School",
            "address": "302 E State St, Millsboro, DE 19966",
            "phone": "302-934-3200",
            "website": "https://www.irsd.net",
            "students": 600
        },
        {
            "school_name": "Selbyville Middle School",
            "address": "80 Bethany Rd, Selbyville, DE 19975",
            "phone": "302-436-1020",
            "website": "https://www.irsd.net",
            "students": 600
        },
        {
            "school_name": "Clayton (John M.) Elementary School",
            "address": "252 Clayton Ave, Frankford, DE 19945",
            "phone": "302-732-3800",
            "website": "https://www.irsd.net",
            "students": 500
        },
        {
            "school_name": "East Millsboro Elementary School",
            "address": "29346 Iron Branch Rd, Millsboro, DE 19966",
            "phone": "302-934-3222",
            "website": "https://www.irsd.net",
            "students": 600
        },
        {
            "school_name": "Georgetown Elementary School",
            "address": "301A W Market St, Georgetown, DE 19947",
            "phone": "302-855-2430",
            "website": "https://www.irsd.net",
            "students": 700
        },
        {
            "school_name": "Long Neck Elementary School",
            "address": "26064 School Ln, Millsboro, DE 19966",
            "phone": "302-945-6200",
            "website": "https://www.irsd.net",
            "students": 550
        },
        {
            "school_name": "Lord Baltimore Elementary School",
            "address": "120 Atlantic Ave, Ocean View, DE 19970",
            "phone": "302-537-2700",
            "website": "https://www.irsd.net",
            "students": 600
        },
        {
            "school_name": "North Georgetown Elementary School",
            "address": "664 N Bedford St, Georgetown, DE 19947",
            "phone": "302-855-2430",
            "website": "https://www.irsd.net",
            "students": 650
        },
        {
            "school_name": "Showell (Phillip C.) Elementary School",
            "address": "41 Bethany Rd, Selbyville, DE 19975",
            "phone": "302-436-1040",
            "website": "https://www.irsd.net",
            "students": 500
        },
        {
            "school_name": "Early Learning Center",
            "address": "206 S Railroad Ave, Georgetown, DE 19947",
            "phone": "302-856-5909",
            "website": "https://www.irsd.net",
            "students": 300
        },
        {
            "school_name": "Ennis (Howard T.) School",
            "address": "20346 Ennis St, Georgetown, DE 19947",
            "phone": "302-856-1930",
            "website": "https://www.irsd.net",
            "students": 100
        },
        {
            "school_name": "Southern Delaware School of the Arts",
            "address": "27 Hosier St, Selbyville, DE 19975",
            "phone": "302-436-1066",
            "website": "https://www.irsd.net",
            "students": 400
        }
    ],
    "Lake Forest School District": [
        {
            "school_name": "Lake Forest High School",
            "address": "5407 Killens Pond Rd, Felton, DE 19943",
            "phone": "302-284-9291",
            "website": "https://www.lf.k12.de.us",
            "students": 1000
        },
        {
            "school_name": "Chipman (W.T.) Middle School",
            "address": "101 W Center St, Harrington, DE 19952",
            "phone": "302-398-8197",
            "website": "https://www.lf.k12.de.us",
            "students": 700
        },
        {
            "school_name": "Lake Forest Central Elementary School",
            "address": "5424 Killens Pond Rd, Felton, DE 19943",
            "phone": "302-284-5810",
            "website": "https://www.lf.k12.de.us",
            "students": 600
        },
        {
            "school_name": "Lake Forest East Elementary School",
            "address": "124 W Front St, Frederica, DE 19946",
            "phone": "302-335-5261",
            "website": "https://www.lf.k12.de.us",
            "students": 500
        },
        {
            "school_name": "Lake Forest North Elementary School",
            "address": "319 E Main St, Felton, DE 19943",
            "phone": "302-284-9611",
            "website": "https://www.lf.k12.de.us",
            "students": 550
        },
        {
            "school_name": "Lake Forest South Elementary School",
            "address": "301 Dorman St, Harrington, DE 19952",
            "phone": "302-398-8011",
            "website": "https://www.lf.k12.de.us",
            "students": 450
        },
        {
            "school_name": "Delaware Early Childhood Center",
            "address": "100 E Liberty St, Harrington, DE 19952",
            "phone": "302-398-8945",
            "website": "https://www.lf.k12.de.us",
            "students": 200
        }
    ],
    "Laurel School District": [
        {
            "school_name": "Laurel High School",
            "address": "1133 S Central Ave, Laurel, DE 19956",
            "phone": "302-875-6120",
            "website": "https://www.laurelschooldistrict.org",
            "students": 700
        },
        {
            "school_name": "Laurel Middle School",
            "address": "1133 S Central Ave, Laurel, DE 19956",
            "phone": "302-875-6110",
            "website": "https://www.laurelschooldistrict.org",
            "students": 600
        },
        {
            "school_name": "North Laurel Elementary School",
            "address": "300 Wilson St, Laurel, DE 19956",
            "phone": "302-875-6140",
            "website": "https://www.laurelschooldistrict.org",
            "students": 500
        }
    ],
    "Milford School District": [
        {
            "school_name": "Milford High School",
            "address": "1019 N Walnut St, Milford, DE 19963",
            "phone": "302-422-1610",
            "website": "https://www.milfordschooldistrict.org",
            "students": 1200
        },
        {
            "school_name": "Milford Central Academy",
            "address": "1021 N Walnut St, Milford, DE 19963",
            "phone": "302-422-1640",
            "website": "https://www.milfordschooldistrict.org",
            "students": 1000
        },
        {
            "school_name": "Banneker (Benjamin) Elementary School",
            "address": "449 North St, Milford, DE 19963",
            "phone": "302-422-1630",
            "website": "https://www.milfordschooldistrict.org",
            "students": 500
        },
        {
            "school_name": "Mispillion Elementary School",
            "address": "311 Lovers Ln, Milford, DE 19963",
            "phone": "302-424-5800",
            "website": "https://www.milfordschooldistrict.org",
            "students": 450
        },
        {
            "school_name": "Ross (Lulu M.) Elementary School",
            "address": "310 Lovers Ln, Milford, DE 19963",
            "phone": "302-422-1640",
            "website": "https://www.milfordschooldistrict.org",
            "students": 500
        },
        {
            "school_name": "Morris (Evelyn I.) Early Childhood Center",
            "address": "8609 Third St, Lincoln, DE 19960",
            "phone": "302-422-1650",
            "website": "https://www.milfordschooldistrict.org",
            "students": 300
        }
    ],
    "New Castle County Vocational-Technical School District": [
        {
            "school_name": "Delcastle Technical High School",
            "address": "1417 Newport Rd, Wilmington, DE 19804",
            "phone": "302-995-8100",
            "website": "https://www.nccvotech.com",
            "students": 1500
        },
        {
            "school_name": "Howard High School of Technology",
            "address": "401 E 12th St, Wilmington, DE 19801",
            "phone": "302-571-5400",
            "website": "https://www.nccvotech.com",
            "students": 900
        },
        {
            "school_name": "St. Georges Technical High School",
            "address": "555 Hyetts Corner Rd, Middletown, DE 19709",
            "phone": "302-449-3360",
            "website": "https://www.nccvotech.com",
            "students": 1200
        },
        {
            "school_name": "Hodgson Vo-Tech High School",
            "address": "2575 Glasgow Ave, Newark, DE 19702",
            "phone": "302-834-0990",
            "website": "https://www.nccvotech.com",
            "students": 1100
        }
    ],
    "Polytech School District": [
        {
            "school_name": "Polytech High School",
            "address": "823 Walnut Shade Rd, Woodside, DE 19980",
            "phone": "302-697-3255",
            "website": "https://www.polytechpanthers.com",
            "students": 1200
        }
    ],
    "Red Clay Consolidated School District": [
        {
            "school_name": "Cab Calloway School of the Arts",
            "address": "100 N DuPont Rd, Wilmington, DE 19807",
            "phone": "302-651-2700",
            "website": "https://www.redclayschools.com",
            "students": 900,
            "grade_levels": "6-12"
        },
        {
            "school_name": "Conrad Schools of Science",
            "address": "201 Jackson Ave, Wilmington, DE 19804",
            "phone": "302-992-5545",
            "website": "https://www.redclayschools.com",
            "students": 1200,
            "grade_levels": "6-12"
        },
        {
            "school_name": "John Dickinson High School",
            "address": "1801 Milltown Rd, Wilmington, DE 19808",
            "phone": "302-992-5500",
            "website": "https://www.redclayschools.com",
            "students": 800,
            "grade_levels": "9-12"
        },
        {
            "school_name": "John Dickinson High School (IB Program)",
            "address": "1801 Milltown Rd, Wilmington, DE 19808",
            "phone": "302-992-5500",
            "website": "https://www.redclayschools.com",
            "students": 300,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Alexis I. duPont High School",
            "address": "50 Hillside Rd, Wilmington, DE 19807",
            "phone": "302-651-2626",
            "website": "https://www.redclayschools.com",
            "students": 1200,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Thomas McKean High School",
            "address": "301 McKennan's Church Rd, Wilmington, DE 19808",
            "phone": "302-992-5520",
            "website": "https://www.redclayschools.com",
            "students": 900,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Charter School of Wilmington",
            "address": "100 N DuPont Rd, Wilmington, DE 19807",
            "phone": "302-651-2727",
            "website": "https://www.charterschoolwilmington.org",
            "students": 970,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Delaware Military Academy",
            "address": "112 Middleboro Rd, Wilmington, DE 19804",
            "phone": "302-998-0745",
            "website": "https://www.demilacademy.org",
            "students": 560,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Alexis I. duPont Middle School",
            "address": "3130 Kennett Pike, Wilmington, DE 19807",
            "phone": "302-651-2690",
            "website": "https://www.redclayschools.com",
            "students": 600,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Henry B. duPont Middle School",
            "address": "735 Meeting House Rd, Hockessin, DE 19707",
            "phone": "302-239-3420",
            "website": "https://www.redclayschools.com",
            "students": 700,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Skyline Middle School",
            "address": "2900 Skyline Dr, Wilmington, DE 19808",
            "phone": "302-454-3410",
            "website": "https://www.redclayschools.com",
            "students": 800,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Stanton Middle School",
            "address": "1800 Limestone Rd, Wilmington, DE 19804",
            "phone": "302-992-5540",
            "website": "https://www.redclayschools.com",
            "students": 650,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Anna P. Mote Elementary School",
            "address": "2110 Edwards Ave, Wilmington, DE 19808",
            "phone": "302-992-5560",
            "website": "https://www.redclayschools.com",
            "students": 500,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Austin D. Baltz Elementary School",
            "address": "1500 Spruce Ave, Wilmington, DE 19805",
            "phone": "302-992-5565",
            "website": "https://www.redclayschools.com",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Brandywine Springs School",
            "address": "2916 Duncan Rd, Wilmington, DE 19808",
            "phone": "302-636-5681",
            "website": "https://www.redclayschools.com",
            "students": 700,
            "grade_levels": "K-8"
        },
        {
            "school_name": "Evan G. Shortlidge Academy",
            "address": "100 W 18th St, Wilmington, DE 19802",
            "phone": "302-651-2710",
            "website": "https://www.redclayschools.com",
            "students": 300,
            "grade_levels": "K-2"
        },
        {
            "school_name": "Forest Oak Elementary School",
            "address": "55 S Meadowood Dr, Newark, DE 19711",
            "phone": "302-454-3425",
            "website": "https://www.redclayschools.com",
            "students": 400,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Heritage Elementary School",
            "address": "2815 Highlands Ln, Wilmington, DE 19808",
            "phone": "302-992-5563",
            "website": "https://www.redclayschools.com",
            "students": 350,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Highlands Elementary School",
            "address": "2100 Gilpin Ave, Wilmington, DE 19806",
            "phone": "302-651-2705",
            "website": "https://www.redclayschools.com",
            "students": 300,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Linden Hill Elementary School",
            "address": "3415 Skyline Dr, Wilmington, DE 19808",
            "phone": "302-454-3406",
            "website": "https://www.redclayschools.com",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Marbrook Elementary School",
            "address": "2101 Centerville Rd, Wilmington, DE 19808",
            "phone": "302-992-5555",
            "website": "https://www.redclayschools.com",
            "students": 400,
            "grade_levels": "K-5"
        },
        {
            "school_name": "North Star Elementary School",
            "address": "1340 Little Baltimore Rd, Hockessin, DE 19707",
            "phone": "302-234-7200",
            "website": "https://www.redclayschools.com",
            "students": 500,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Richardson Park Elementary School",
            "address": "16 Idella Ave, Wilmington, DE 19804",
            "phone": "302-992-5570",
            "website": "https://www.redclayschools.com",
            "students": 350,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Donald J. Richey Elementary School",
            "address": "105 E Highland Blvd, New Castle, DE 19720",
            "phone": "302-429-4164",
            "website": "https://www.redclayschools.com",
            "students": 300,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Warner Elementary School",
            "address": "801 W 18th St, Wilmington, DE 19802",
            "phone": "302-651-2740",
            "website": "https://www.redclayschools.com",
            "students": 400,
            "grade_levels": "3-5"
        },
        {
            "school_name": "William C. Lewis Dual Language Elementary School",
            "address": "920 N Van Buren St, Wilmington, DE 19806",
            "phone": "302-651-2695",
            "website": "https://www.redclayschools.com",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "William Cooke, Jr. Elementary School",
            "address": "2025 Graves Rd, Hockessin, DE 19707",
            "phone": "302-235-6600",
            "website": "https://www.redclayschools.com",
            "students": 500,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Red Clay Early Years Program",
            "address": "1621 Telegraph Rd, Wilmington, DE 19804",
            "phone": "302-992-5562",
            "website": "https://www.redclayschools.com",
            "students": 150,
            "grade_levels": "PreK"
        },
        {
            "school_name": "First State School",
            "address": "501 W 14th St, Wilmington, DE 19801",
            "phone": "302-428-5845",
            "website": "https://www.redclayschools.com",
            "students": 50,
            "grade_levels": "2-12"
        },
        {
            "school_name": "James H. Groves Adult High School",
            "address": "2220 Shipley Rd, Wilmington, DE 19803",
            "phone": "302-651-2704",
            "website": "https://www.redclayschools.com",
            "students": 200,
            "grade_levels": "Adult Education"
        },
        {
            "school_name": "Meadowood Program",
            "address": "55 S Meadowood Dr, Newark, DE 19711",
            "phone": "302-454-3400",
            "website": "https://www.redclayschools.com",
            "students": 100,
            "grade_levels": "3-21"
        }
    ],
    "Seaford School District": [
        {
            "school_name": "Seaford High School",
            "address": "399 N Market St Ext, Seaford, DE 19973",
            "phone": "302-629-4587",
            "website": "https://www.seafordbluejays.org",
            "students": 800,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Seaford Middle School",
            "address": "500 E Stein Hwy, Seaford, DE 19973",
            "phone": "302-629-4585",
            "website": "https://www.seafordbluejays.org",
            "students": 600,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Blades Elementary School",
            "address": "900 S Arch St, Blades, DE 19973",
            "phone": "302-628-4416",
            "website": "https://www.seafordbluejays.org",
            "students": 450,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Frederick Douglass Elementary School",
            "address": "1 Swain Rd, Seaford, DE 19973",
            "phone": "302-629-4586",
            "website": "https://www.seafordbluejays.org",
            "students": 400,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Seaford Central Elementary School",
            "address": "1 Delaware Pl, Seaford, DE 19973",
            "phone": "302-629-4587",
            "website": "https://www.seafordbluejays.org",
            "students": 350,
            "grade_levels": "K-5"
        },
        {
            "school_name": "West Seaford Elementary School",
            "address": "511 Sussex Ave, Seaford, DE 19973",
            "phone": "302-629-9352",
            "website": "https://www.seafordbluejays.org",
            "students": 400,
            "grade_levels": "K-5"
        }
    ],
    "Smyrna School District": [
        {
            "school_name": "Smyrna High School",
            "address": "500 Duck Creek Pkwy, Smyrna, DE 19977",
            "phone": "302-653-8581",
            "website": "https://www.smyrna.k12.de.us",
            "students": 1600,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Smyrna Middle School",
            "address": "700 Duck Creek Pkwy, Smyrna, DE 19977",
            "phone": "302-653-8584",
            "website": "https://www.smyrna.k12.de.us",
            "students": 800,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Clayton Intermediate School",
            "address": "86 S Bassett St, Clayton, DE 19938",
            "phone": "302-659-6297",
            "website": "https://www.smyrna.k12.de.us",
            "students": 600,
            "grade_levels": "4-5"
        },
        {
            "school_name": "John Bassett Moore Intermediate School",
            "address": "20 W Frazier St, Smyrna, DE 19977",
            "phone": "302-653-3134",
            "website": "https://www.smyrna.k12.de.us",
            "students": 500,
            "grade_levels": "4-5"
        },
        {
            "school_name": "Clayton Elementary School",
            "address": "510 W Main St, Clayton, DE 19938",
            "phone": "302-653-8587",
            "website": "https://www.smyrna.k12.de.us",
            "students": 450,
            "grade_levels": "K-3"
        },
        {
            "school_name": "North Smyrna Elementary School",
            "address": "365 N Main St, Smyrna, DE 19977",
            "phone": "302-653-8589",
            "website": "https://www.smyrna.k12.de.us",
            "students": 400,
            "grade_levels": "K-3"
        },
        {
            "school_name": "Smyrna Elementary School",
            "address": "121 S School Ln, Smyrna, DE 19977",
            "phone": "302-653-8588",
            "website": "https://www.smyrna.k12.de.us",
            "students": 500,
            "grade_levels": "K-3"
        },
        {
            "school_name": "Sunnyside Elementary School",
            "address": "123 Rabbit Chase Ln, Smyrna, DE 19977",
            "phone": "302-653-8583",
            "website": "https://www.smyrna.k12.de.us",
            "students": 450,
            "grade_levels": "K-3"
        }
    ],
    "Sussex Technical School District": [
        {
            "school_name": "Sussex Technical High School",
            "address": "17099 County Seat Hwy, Georgetown, DE 19947",
            "phone": "302-856-0961",
            "website": "https://www.sussexvt.k12.de.us",
            "students": 1200
        }
    ],
    "Woodbridge School District": [
        {
            "school_name": "Woodbridge High School",
            "address": "14712 Woodbridge Rd, Greenwood, DE 19950",
            "phone": "302-232-3333",
            "website": "https://www.woodbridgeraiders.net",
            "students": 800,
            "grade_levels": "9-12"
        },
        {
            "school_name": "Woodbridge Middle School",
            "address": "307 Laws St, Bridgeville, DE 19933",
            "phone": "302-337-8289",
            "website": "https://www.woodbridgeraiders.net",
            "students": 600,
            "grade_levels": "6-8"
        },
        {
            "school_name": "Phillis Wheatley Elementary School",
            "address": "48 Church St, Bridgeville, DE 19933",
            "phone": "302-337-3469",
            "website": "https://www.woodbridgeraiders.net",
            "students": 500,
            "grade_levels": "K-5"
        },
        {
            "school_name": "Woodbridge Early Childhood Education Center",
            "address": "400 Governors Ave, Greenwood, DE 19950",
            "phone": "302-349-4539",
            "website": "https://www.woodbridgeraiders.net",
            "students": 300,
            "grade_levels": "PreK-1"
        }
    ],
    "Other": [
        {
            "school_name": "Academia Antonia Alonso",
            "address": "300 N Wakefield Dr., Newark, DE 19702",
            "phone": "302-351-8200",
            "website": "https://academiacharterschool.org/school-information",
            "students": 718
        },
        {
            "school_name": "Academy Of Dover Charter School",
            "address": "104 Saulsbury Road, Dover, DE 19904",
            "phone": "302-674-0684",
            "website": "https://aodcharter.org",
            "students": 700
        },
        {
            "school_name": "Campus Community Charter School",
            "address": "350 Pear St, Dover, DE 19904",
            "phone": "302-736-5555",
            "website": "https://www.campuscommunityschool.com",
            "students": 650
        },
        {
            "school_name": "Charter School of New Castle",
            "address": "1200 Industrial Blvd, New Castle, DE 19720",
            "phone": "302-324-8901",
            "website": "https://www.charterschoolnewcastle.com",
            "students": 450
        },
        {
            "school_name": "Delaware Academy Of Public Safety And Security",
            "address": "109 Wilbur St, Wilmington, DE 19801",
            "phone": "302-995-8100",
            "website": "https://dapass.org",
            "students": 300
        },
        {
            "school_name": "Delaware College Preparatory Academy",
            "address": "510 W 28th St, Wilmington, DE 19802",
            "phone": "302-576-3300",
            "website": "https://www.decp.org",
            "students": 550
        },
        {
            "school_name": "Delaware Design-Lab High School",
            "address": "179 Stanton Christiana Rd, Newark, DE 19713",
            "phone": "302-292-1463",
            "website": "https://www.delawaydesignlabhigh.org",
            "students": 600
        },
        {
            "school_name": "Early College High School at Delaware State University",
            "address": "1200 N DuPont Hwy, Dover, DE 19901",
            "phone": "302-857-7055",
            "website": "https://www.desu.edu/early-college-high-school",
            "students": 300
        },
        {
            "school_name": "East Side Charter School",
            "address": "3000 N Claymont St, Wilmington, DE 19802",
            "phone": "302-762-5834",
            "website": "https://www.eastsidecharterschool.org",
            "students": 450
        },
        {
            "school_name": "Edison (Thomas A.) Charter School",
            "address": "2200 N Locust St, Wilmington, DE 19802",
            "phone": "302-778-1101",
            "website": "https://www.edisontcs.org",
            "students": 700
        },
        {
            "school_name": "First State Military Academy",
            "address": "355 W Duck Creek Rd, Clayton, DE 19938",
            "phone": "302-223-2150",
            "website": "https://www.fsmilitary.org",
            "students": 400,
            
        },
        {
            "school_name": "First State Montessori Academy",
            "address": "1000 N French St, Wilmington, DE 19801",
            "phone": "302-576-1500",
            "website": "https://firststatemontessori.org",
            "students": 600,
            
        },
        {
            "school_name": "Freire Charter School",
            "address": "201 W 14th St, Wilmington, DE 19801",
            "phone": "302-407-4800",
            "website": "https://www.freirewilmington.org",
            "students": 500,
            
        },
        {
            "school_name": "Gateway Lab School",
            "address": "2501 Centerville Rd, Wilmington, DE 19808",
            "phone": "302-633-4091",
            "website": "https://www.gatewaylabschool.org",
            "students": 250,
            
        },
        {
            "school_name": "Great Oaks Charter School",
            "address": "1200 N French St, Wilmington, DE 19801",
            "phone": "302-660-4790",
            "website": "https://www.greatoakscharter.org/wilmington",
            "students": 500,
            
        },
        {
            "school_name": "Kuumba Academy Charter School",
            "address": "1200 N French St, Wilmington, DE 19801",
            "phone": "302-660-4750",
            "website": "https://www.kuumbaacademy.org",
            "students": 600,
            
        },
        {
            "school_name": "Las Americas Aspira Academy",
            "address": "326 Ruthar Dr, Newark, DE 19711",
            "phone": "302-292-1463",
            "website": "https://www.aspiraacademy.org",
            "students": 600,
            
        },
        {
            "school_name": "Moyer (Maurice J.) Academy",
            "address": "610 E 17th St, Wilmington, DE 19802",
            "phone": "302-428-9500",
            "website": "https://www.moyeracademy.org",
            "students": 300,
            
        },
        {
            "school_name": "Mot Charter School",
            "address": "1156 Levels Rd, Middletown, DE 19709",
            "phone": "302-376-5125",
            "website": "https://www.motcharter.com",
            "students": 1200,
            
        },
        {
            "school_name": "Newark Charter School",
            "address": "2001 Patriot Way, Newark, DE 19711",
            "phone": "302-369-2001",
            "website": "https://www.newarkcharterschool.org",
            "students": 2300,
            
        },
        {
            "school_name": "Odyssey Charter School",
            "address": "4319 Lancaster Pike, Wilmington, DE 19805",
            "phone": "302-994-6490",
            "website": "https://www.odysseycharterschooldel.com",
            "students": 1800,
            
        },
        {
            "school_name": "Positive Outcomes Charter School",
            "address": "3337 S DuPont Hwy, Camden, DE 19934",
            "phone": "302-697-8805",
            "website": "https://www.positiveoutcomescs.org",
            "students": 120,
            
        },
        {
            "school_name": "Prestige Academy",
            "address": "1121 Thatcher St, Wilmington, DE 19802",
            "phone": "302-276-5078",
            "website": "https://www.prestigeacademycs.org",
            "students": 300,
            
        },
        {
            "school_name": "Providence Creek Academy Charter School",
            "address": "355 W Duck Creek Rd, Clayton, DE 19938",
            "phone": "302-653-6276",
            "website": "https://www.pcasaints.org",
            "students": 700,
            
        },
        {
            "school_name": "Reach Academy For Girls",
            "address": "170 Lukens Dr, New Castle, DE 19720",
            "phone": "302-654-2495",
            "website": "https://www.reachacademyforgirls.org",
            "students": 400,
            
        },
        {
            "school_name": "Sussex Academy",
            "address": "21150 Airport Rd, Georgetown, DE 19947",
            "phone": "302-856-3636",
            "website": "https://www.sussexacademy.org",
            "students": 800,

        },
        {
            "school_name": "Sussex Montessori School",
            "address": "24960 Dairy Ln, Seaford, DE 19973",
            "phone": "302-404-5367",
            "website": "https://www.sussexmontessoricharter.com",
            "students": 300,
            
        }
    ]
}

# Combine all school lists into one DataFrame
schools_data = pd.DataFrame([school for district in schools.values() for school in district])

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Assign district names to each row in the DataFrame
for district_name, schools_list in schools.items():
    district_name = district_name.replace(" Dist.", "").replace(" Public School District", "").replace(" School District", "").replace(" School Dist", "").replace(" Public School", "").replace(" District", "").rstrip('.')

    for school in schools_list:
        school['address'] = school['address'].replace('+', ', ')
        schools_data.loc[schools_data['school_name'] == school['school_name'], 'district_name'] = district_name

# Function to generate markdown files
def generate_markdown_by_index(row):
    # Simplify the school name for the directory and file
    district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    path = os.path.join(output_dir, district_name_simple)
    os.makedirs(path, exist_ok=True)

    # Filename for the markdown
    file_path = os.path.join(path, f"{school_name_simple}.md")

    # Markdown content with front-matter and details
    with open(file_path, 'w') as file:
        file.write(f"---\nlayout: page\ntitle: {row['school_name']}\n---\n")  # School Name
        file.write(
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All Deleware Districts]](../..) > [[All In {row['district_name']}]](..)\n\n")

        file.write(f"# {row['school_name']} ({row['district_name']})\n\n")  # School Name and area as header

        # Loop through keys per school
        for key, value in row.items():
            if key not in ['district_name', 'school_name']:
                if str(value).startswith("http"):
                    value = "<" + value + ">"
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")

        file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        file.write(f"**School's policy on Ventilation**: TODO\n\n")
        file.write(f"**School's Ventilation Work Completion**: TODO\n\n")
        file.write(f"**School's Air-Purification**: TODO\n\n")
        file.write(f"**School's CO2 monitoring to actively drive ventilation and filtration**: TODO\n\n")
        file.write(f"**School's Wikidata URL**: TODO")
        file.write(f"\n\n\n[Edit this page](https://github.com/ventilate-schools/DE/edit/main/{file_path}).")
        file.write(f" See also [rules for contribution](../../../contribution-rules/)")

# Generate markdown files for each school
schools_data.apply(generate_markdown_by_index, axis=1)

def create_area_and_root_index():
    # Create a dictionary to keep track of schools in each district
    districts_dict = {}

    for index, row in schools_data.iterrows():
        district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
        school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the district already exists in the dictionary
        if district_name_simple not in districts_dict:
            districts_dict[district_name_simple] = []

        # Append the school name to the district's list
        districts_dict[district_name_simple].append(school_name_simple)

    # Write an index markdown file for each district and gather data for root index
    root_index_content = "---\ntitle: Schools in Deleware and their ventilation status\n---\n"

    root_index_content += (
        "\n# Navigation\n\n[[All countries/states/provinces]](..)\n\n# Purpose of site\n\nGiven **COVID-19 is Airborne** and the world is pushing to better ventilate "
        "schools for long term student and teacher health, we're tracking the "
        "progress for that in Deleware. This is ahead of government effort to do the same. If government starts to "
        "track this work, this effort will continue because that effort might be weak."
        "We're guided by 33 profs and PhDs who are pushing for a policy change in a "
        "March 2024 article on **Science.org**: [Mandating indoor air quality for public buildings](https://drive.google.com/file/d/16l_IH47cQtC7fFuafvHca7ORNVGITxx8/view). "
        "Not only active ventilation (which should "
        "be mechanical heat recovery type in this age), but air filtration/purification "
        "too and CO2 monitoring to drive ventilation levels, as CO2 inside is a proxy indicator "
        "for COVID risk. As it happens the WHO also have a [2023 airborne risk assessment guide](https://iris.who.int/handle/10665/376346)\n\n"
        "Know that other diseases are airborne too: Measles "
        "(studies [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810934/pdf/10982072.pdf) "
        "[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880795/pdf/nihms532643.pdf) "
        "[3](https://pubmed.ncbi.nlm.nih.gov/31257413/) "
        "[4](https://www.sciencedirect.com/science/article/pii/S0196655316305363)), "
        "Influenza, RSV and TB. The same "
        "ventilation and air filtration measures reduce transmission of those too.\n\n When we say "
        "student and teacher health, we're wanting absences to go down too. If we lower "
        "transmission in schools, we reduce multi-generation transmission too, as kids bring "
        "infections home to parents. With lowered transmission, we also reduce long COVID, "
        "where the worst sufferers have disappeared from education and the workplace.\n\n")

    root_index_content += (
        "\n## Leaderboard\n\n1. to be announced\n2. to be announced\n3. to be announced\n4. to be announced\n5. to be announced\n\n")

    root_index_content += ("{% include_relative grade.html %}\n\n")

    root_index_content += ("# Deleware School Districts:\n\n")

    for district, schools in districts_dict.items():
        district_index_file_path = os.path.join(output_dir, district, "index.md")
        os.makedirs(os.path.join(output_dir, district), exist_ok=True)

        with open(district_index_file_path, 'w') as district_index_file:
            district_index_file.write(f"---\nlayout: page\ntitle: Schools in {district.replace('_', ' ')}\n---\n")
            district_index_file.write(
                f"# Navigation\n\n[[All countries/states/provinces]](../..) > [[All B.C. districts]](..)\n\n")
            district_index_file.write(f"# Schools in {district.replace('_', ' ')}\n\n")
            district_index_file.write("{% include_relative grade.html %}\n\n")
            district_index_file.write(f"**Schools:**\n\n")
            for school in schools:
                school_file_path = school
                district_index_file.write(f"- [{school.replace('_', ' ')}]({school_file_path}.md)\n")

        # Add to root index content with cleaner URLs
        root_index_content += f"- [{district.replace('_', ' ')}]({district}/): {len(schools)} schools\n"

    root_index_content += ("\n\n# Site ownership\n\nThis site is edited by volunteers who're "
                           "interested in accelerating the work to complete the adequate ventilation of Deleware schools. "
                           "This effort was not commissioned by education authorities or government.\n\n"
                           "[Edit this page](https://github.com/ventilate-schools/DE/edit/main/index.md). See also [rules for contribution](./contribution_rules/)")

    # Write the root index file
    root_index_path = os.path.join(output_dir, "index.md")
    with open(root_index_path, 'w') as root_index_file:
        root_index_file.write(root_index_content)

# Call the function to create index markdown files and root index
create_area_and_root_index()

# Print confirmation
print("Index markdown files with front matter and links have been created in each area directory and root directory.")