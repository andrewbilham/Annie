import requests

# The provided JSON data
data = [
  {
    "source_id": 7,
    "type": "Taxi",
    "daystohire": 7,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "John",
    "client_lastname": "Doe",
    "client_address_1": "123 Elm Street",
    "client_address_town": "Springfield",
    "client_address_postcode": "SP1 2AB",
    "client_vehicle_reg": "AB12CDE",
    "client_insurer": "Acme Insurance",
    "client_insurer_policyno": "POL1234567",
    "client_phone": "0123456789",
    "client_mobile": "07123456789",
    "client_email": "john.doe@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-27",
    "accident_time": "09:33:34.413Z",
    "accident_location": "456 Oak Avenue",
    "accident_circs": "Rear-end collision",
    "tp_firstname": "Jane",
    "tp_lastname": "Smith",
    "tp_address_1": "789 Pine Road",
    "tp_address_town": "Shelbyville",
    "tp_address_postcode": "SH1 3CD",
    "tp_vehicle_reg": "XY34ZRT",
    "tp_insurer": "Umbrella Corp Insurance",
    "tp_insurer_polcyno": "POL7654321",
    "tp_phone": "0987654321",
    "tp_mobile": "07876543210"
  },
  {
    "source_id": 14,
    "type": "Taxi",
    "daystohire": 8,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Alice",
    "client_lastname": "Brown",
    "client_address_1": "456 Maple Street",
    "client_address_town": "Greenfield",
    "client_address_postcode": "GF2 3HJ",
    "client_vehicle_reg": "CD34EFG",
    "client_insurer": "Beta Insurance",
    "client_insurer_policyno": "POL2345678",
    "client_phone": "0234567890",
    "client_mobile": "07234567890",
    "client_email": "alice.brown@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-26",
    "accident_time": "10:22:41.527Z",
    "accident_location": "789 Cedar Avenue",
    "accident_circs": "Side collision",
    "tp_firstname": "Bob",
    "tp_lastname": "Jones",
    "tp_address_1": "123 Oak Lane",
    "tp_address_town": "Clearwater",
    "tp_address_postcode": "CW4 5KL",
    "tp_vehicle_reg": "GH56IJK",
    "tp_insurer": "Gamma Insurance",
    "tp_insurer_polcyno": "POL8765432",
    "tp_phone": "0456789012",
    "tp_mobile": "07987654321"
  },
  {
    "source_id": 21,
    "type": "Taxi",
    "daystohire": 5,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Charlie",
    "client_lastname": "Davis",
    "client_address_1": "789 Pine Street",
    "client_address_town": "Hilltop",
    "client_address_postcode": "HT3 6MN",
    "client_vehicle_reg": "EF78HIJ",
    "client_insurer": "Delta Insurance",
    "client_insurer_policyno": "POL3456789",
    "client_phone": "0345678901",
    "client_mobile": "07345678901",
    "client_email": "charlie.davis@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-25",
    "accident_time": "11:11:11.111Z",
    "accident_location": "321 Birch Boulevard",
    "accident_circs": "Hit and run",
    "tp_firstname": "David",
    "tp_lastname": "Williams",
    "tp_address_1": "456 Elm Lane",
    "tp_address_town": "Riverside",
    "tp_address_postcode": "RS5 7OP",
    "tp_vehicle_reg": "IJ90KLM",
    "tp_insurer": "Epsilon Insurance",
    "tp_insurer_polcyno": "POL9876543",
    "tp_phone": "0567890123",
    "tp_mobile": "07123456789"
  },
  {
    "source_id": 11,
    "type": "Taxi",
    "daystohire": 10,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Diana",
    "client_lastname": "Evans",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Riverwood",
    "client_address_postcode": "RW8 9QR",
    "client_vehicle_reg": "GH12JKL",
    "client_insurer": "Epsilon Insurance",
    "client_insurer_policyno": "POL4567890",
    "client_phone": "0456789012",
    "client_mobile": "07456789012",
    "client_email": "diana.evans@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-24",
    "accident_time": "12:22:33.444Z",
    "accident_location": "654 Maple Avenue",
    "accident_circs": "Rear-end collision",
    "tp_firstname": "Emily",
    "tp_lastname": "Johnson",
    "tp_address_1": "789 Oak Road",
    "tp_address_town": "Hillview",
    "tp_address_postcode": "HV6 8QR",
    "tp_vehicle_reg": "KL12MNO",
    "tp_insurer": "Zeta Insurance",
    "tp_insurer_polcyno": "POL7654321",
    "tp_phone": "0678901234",
    "tp_mobile": "07234567890"
  },
  {
    "source_id": 8,
    "type": "Taxi",
    "daystohire": 3,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Edward",
    "client_lastname": "Brown",
    "client_address_1": "654 Maple Street",
    "client_address_town": "Clearwater",
    "client_address_postcode": "CW2 4TU",
    "client_vehicle_reg": "MN12OPQ",
    "client_insurer": "Gamma Insurance",
    "client_insurer_policyno": "POL5678901",
    "client_phone": "0678901234",
    "client_mobile": "07345678901",
    "client_email": "edward.brown@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-23",
    "accident_time": "13:33:44.555Z",
    "accident_location": "987 Pine Lane",
    "accident_circs": "Side collision",
    "tp_firstname": "Frank",
    "tp_lastname": "Thompson",
    "tp_address_1": "123 Elm Avenue",
    "tp_address_town": "Greenwood",
    "tp_address_postcode": "GW4 5TU",
    "tp_vehicle_reg": "OP34QRS",
    "tp_insurer": "Theta Insurance",
    "tp_insurer_polcyno": "POL6543210",
    "tp_phone": "0789012345",
    "tp_mobile": "07456789012"
  },
  {
    "source_id": 17,
    "type": "Taxi",
    "daystohire": 9,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Fiona",
    "client_lastname": "Green",
    "client_address_1": "789 Oak Street",
    "client_address_town": "Shelbyville",
    "client_address_postcode": "SH5 6WX",
    "client_vehicle_reg": "QR56STU",
    "client_insurer": "Theta Insurance",
    "client_insurer_policyno": "POL6789012",
    "client_phone": "0789012345",
    "client_mobile": "07567890123",
    "client_email": "fiona.green@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-22",
    "accident_time": "14:44:55.666Z",
    "accident_location": "321 Birch Lane",
    "accident_circs": "Hit and run",
    "tp_firstname": "George",
    "tp_lastname": "White",
    "tp_address_1": "654 Maple Road",
    "tp_address_town": "Riverwood",
    "tp_address_postcode": "RW7 8YZ",
    "tp_vehicle_reg": "ST78UVW",
    "tp_insurer": "Lambda Insurance",
    "tp_insurer_polcyno": "POL5432109",
    "tp_phone": "0890123456",
    "tp_mobile": "07678901234"
  },
  {
    "source_id": 3,
    "type": "Taxi",
    "daystohire": 6,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "George",
    "client_lastname": "Harris",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Hilltop",
    "client_address_postcode": "HT8 9QR",
    "client_vehicle_reg": "VW90XYZ",
    "client_insurer": "Zeta Insurance",
    "client_insurer_policyno": "POL7890123",
    "client_phone": "0890123456",
    "client_mobile": "07789012345",
    "client_email": "george.harris@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-21",
    "accident_time": "15:55:11.777Z",
    "accident_location": "987 Pine Boulevard",
    "accident_circs": "Rear-end collision",
    "tp_firstname": "Hannah",
    "tp_lastname": "Martinez",
    "tp_address_1": "123 Elm Lane",
    "tp_address_town": "Springfield",
    "tp_address_postcode": "SP4 5WX",
    "tp_vehicle_reg": "XY12ABC",
    "tp_insurer": "Alpha Insurance",
    "tp_insurer_polcyno": "POL4321098",
    "tp_phone": "0901234567",
    "tp_mobile": "07890123456"
  },
  {
    "source_id": 12,
    "type": "Taxi",
    "daystohire": 4,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Hannah",
    "client_lastname": "Martinez",
    "client_address_1": "654 Maple Street",
    "client_address_town": "Riverside",
    "client_address_postcode": "RS2 3HJ",
    "client_vehicle_reg": "ABC34DEF",
    "client_insurer": "Beta Insurance",
    "client_insurer_policyno": "POL8901234",
    "client_phone": "0901234567",
    "client_mobile": "07901234567",
    "client_email": "hannah.martinez@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-20",
    "accident_time": "16:11:22.888Z",
    "accident_location": "321 Birch Avenue",
    "accident_circs": "Side collision",
    "tp_firstname": "Ian",
    "tp_lastname": "Lewis",
    "tp_address_1": "789 Pine Lane",
    "tp_address_town": "Hillview",
    "tp_address_postcode": "HV5 6WX",
    "tp_vehicle_reg": "DEF56GHI",
    "tp_insurer": "Gamma Insurance",
    "tp_insurer_polcyno": "POL3210987",
    "tp_phone": "0123456789",
    "tp_mobile": "07012345678"
  },
  {
    "source_id": 26,
    "type": "Taxi",
    "daystohire": 7,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Ivy",
    "client_lastname": "Nelson",
    "client_address_1": "987 Pine Street",
    "client_address_town": "Clearwater",
    "client_address_postcode": "CW1 2AB",
    "client_vehicle_reg": "GHI78JKL",
    "client_insurer": "Delta Insurance",
    "client_insurer_policyno": "POL9012345",
    "client_phone": "0123456789",
    "client_mobile": "07123456789",
    "client_email": "ivy.nelson@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-19",
    "accident_time": "17:22:33.999Z",
    "accident_location": "654 Maple Boulevard",
    "accident_circs": "Hit and run",
    "tp_firstname": "Jack",
    "tp_lastname": "Robinson",
    "tp_address_1": "321 Birch Lane",
    "tp_address_town": "Greenfield",
    "tp_address_postcode": "GF4 5WX",
    "tp_vehicle_reg": "GHI90JKL",
    "tp_insurer": "Zeta Insurance",
    "tp_insurer_polcyno": "POL2109876",
    "tp_phone": "0345678901",
    "tp_mobile": "07234567890"
  },
  {
    "source_id": 9,
    "type": "Taxi",
    "daystohire": 10,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Jack",
    "client_lastname": "Robinson",
    "client_address_1": "654 Maple Street",
    "client_address_town": "Hilltop",
    "client_address_postcode": "HT1 2CD",
    "client_vehicle_reg": "JKL12MNO",
    "client_insurer": "Epsilon Insurance",
    "client_insurer_policyno": "POL0123456",
    "client_phone": "0234567890",
    "client_mobile": "07345678901",
    "client_email": "jack.robinson@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-18",
    "accident_time": "18:33:44.000Z",
    "accident_location": "987 Pine Avenue",
    "accident_circs": "Rear-end collision",
    "tp_firstname": "Karen",
    "tp_lastname": "Lopez",
    "tp_address_1": "123 Elm Road",
    "tp_address_town": "Riverwood",
    "tp_address_postcode": "RW3 4ST",
    "tp_vehicle_reg": "MNO34PQR",
    "tp_insurer": "Alpha Insurance",
    "tp_insurer_polcyno": "POL1098765",
    "tp_phone": "0456789012",
    "tp_mobile": "07456789012"
  },
  {
    "source_id": 5,
    "type": "Taxi",
    "daystohire": 6,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Liam",
    "client_lastname": "Wright",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Clearwater",
    "client_address_postcode": "CW3 4ST",
    "client_vehicle_reg": "PQR56STU",
    "client_insurer": "Beta Insurance",
    "client_insurer_policyno": "POL1234567",
    "client_phone": "0567890123",
    "client_mobile": "07567890123",
    "client_email": "liam.wright@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-17",
    "accident_time": "19:44:55.111Z",
    "accident_location": "654 Maple Lane",
    "accident_circs": "Side collision",
    "tp_firstname": "Linda",
    "tp_lastname": "Clark",
    "tp_address_1": "789 Oak Avenue",
    "tp_address_town": "Shelbyville",
    "tp_address_postcode": "SH2 3HJ",
    "tp_vehicle_reg": "ST78UVW",
    "tp_insurer": "Gamma Insurance",
    "tp_insurer_polcyno": "POL3210987",
    "tp_phone": "0678901234",
    "tp_mobile": "07678901234"
  },
  {
    "source_id": 16,
    "type": "Taxi",
    "daystohire": 8,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Mia",
    "client_lastname": "Walker",
    "client_address_1": "654 Maple Street",
    "client_address_town": "Riverside",
    "client_address_postcode": "RS4 5WX",
    "client_vehicle_reg": "UVW90XYZ",
    "client_insurer": "Delta Insurance",
    "client_insurer_policyno": "POL2345678",
    "client_phone": "0789012345",
    "client_mobile": "07789012345",
    "client_email": "mia.walker@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-16",
    "accident_time": "20:55:11.222Z",
    "accident_location": "987 Pine Road",
    "accident_circs": "Hit and run",
    "tp_firstname": "Nancy",
    "tp_lastname": "Hill",
    "tp_address_1": "321 Birch Boulevard",
    "tp_address_town": "Greenfield",
    "tp_address_postcode": "GF2 3HJ",
    "tp_vehicle_reg": "XYZ12ABC",
    "tp_insurer": "Zeta Insurance",
    "tp_insurer_polcyno": "POL0987654",
    "tp_phone": "0890123456",
    "tp_mobile": "07890123456"
  },
  {
    "source_id": 13,
    "type": "Taxi",
    "daystohire": 7,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Olivia",
    "client_lastname": "Young",
    "client_address_1": "987 Pine Street",
    "client_address_town": "Hilltop",
    "client_address_postcode": "HT5 6WX",
    "client_vehicle_reg": "ABC12DEF",
    "client_insurer": "Epsilon Insurance",
    "client_insurer_policyno": "POL3456789",
    "client_phone": "0123456789",
    "client_mobile": "07123456789",
    "client_email": "olivia.young@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-15",
    "accident_time": "21:11:22.333Z",
    "accident_location": "654 Maple Avenue",
    "accident_circs": "Rear-end collision",
    "tp_firstname": "Paul",
    "tp_lastname": "Martin",
    "tp_address_1": "123 Elm Road",
    "tp_address_town": "Springfield",
    "tp_address_postcode": "SP4 5WX",
    "tp_vehicle_reg": "DEF34GHI",
    "tp_insurer": "Alpha Insurance",
    "tp_insurer_polcyno": "POL4321098",
    "tp_phone": "0345678901",
    "tp_mobile": "07234567890"
  },
  {
    "source_id": 22,
    "type": "Taxi",
    "daystohire": 5,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Paul",
    "client_lastname": "Martin",
    "client_address_1": "654 Maple Street",
    "client_address_town": "Clearwater",
    "client_address_postcode": "CW1 2CD",
    "client_vehicle_reg": "GHI56JKL",
    "client_insurer": "Gamma Insurance",
    "client_insurer_policyno": "POL5678901",
    "client_phone": "0456789012",
    "client_mobile": "07345678901",
    "client_email": "paul.martin@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-14",
    "accident_time": "22:22:33.444Z",
    "accident_location": "321 Birch Lane",
    "accident_circs": "Side collision",
    "tp_firstname": "Quinn",
    "tp_lastname": "King",
    "tp_address_1": "987 Pine Road",
    "tp_address_town": "Hillview",
    "tp_address_postcode": "HV3 4ST",
    "tp_vehicle_reg": "JKL78MNO",
    "tp_insurer": "Lambda Insurance",
    "tp_insurer_polcyno": "POL0987654",
    "tp_phone": "0567890123",
    "tp_mobile": "07567890123"
  },
  {
    "source_id": 24,
    "type": "Taxi",
    "daystohire": 10,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Quinn",
    "client_lastname": "King",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Riverwood",
    "client_address_postcode": "RW5 6WX",
    "client_vehicle_reg": "MNO90PQR",
    "client_insurer": "Beta Insurance",
    "client_insurer_policyno": "POL6789012",
    "client_phone": "0678901234",
    "client_mobile": "07678901234",
    "client_email": "quinn.king@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-13",
    "accident_time": "23:33:44.555Z",
    "accident_location": "654 Maple Boulevard",
    "accident_circs": "Hit and run",
    "tp_firstname": "Rebecca",
    "tp_lastname": "Scott",
    "tp_address_1": "123 Elm Avenue",
    "tp_address_town": "Shelbyville",
    "tp_address_postcode": "SH1 2AB",
    "tp_vehicle_reg": "PQR12STU",
    "tp_insurer": "Theta Insurance",
    "tp_insurer_polcyno": "POL5432109",
    "tp_phone": "0789012345",
    "tp_mobile": "07789012345"
  },
  {
    "source_id": 27,
    "type": "Taxi",
    "daystohire": 7,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Rebecca",
    "client_lastname": "Scott",
    "client_address_1": "654 Maple Street",
    "client_address_town": "Greenfield",
    "client_address_postcode": "GF1 2AB",
    "client_vehicle_reg": "ST34UVW",
    "client_insurer": "Alpha Insurance",
    "client_insurer_policyno": "POL7890123",
    "client_phone": "0123456789",
    "client_mobile": "07123456789",
    "client_email": "rebecca.scott@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-12",
    "accident_time": "09:11:22.666Z",
    "accident_location": "987 Pine Lane",
    "accident_circs": "Rear-end collision",
    "tp_firstname": "Samuel",
    "tp_lastname": "Turner",
    "tp_address_1": "321 Birch Avenue",
    "tp_address_town": "Clearwater",
    "tp_address_postcode": "CW3 4ST",
    "tp_vehicle_reg": "UVW56XYZ",
    "tp_insurer": "Gamma Insurance",
    "tp_insurer_polcyno": "POL2109876",
    "tp_phone": "0234567890",
    "tp_mobile": "07234567890"
  },
  {
    "source_id": 1,
    "type": "Taxi",
    "daystohire": 9,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Samuel",
    "client_lastname": "Turner",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Riverwood",
    "client_address_postcode": "RW2 3HJ",
    "client_vehicle_reg": "XYZ90ABC",
    "client_insurer": "Delta Insurance",
    "client_insurer_policyno": "POL8901234",
    "client_phone": "0345678901",
    "client_mobile": "07345678901",
    "client_email": "samuel.turner@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-11",
    "accident_time": "10:22:33.777Z",
    "accident_location": "654 Maple Road",
    "accident_circs": "Side collision",
    "tp_firstname": "Thomas",
    "tp_lastname": "Young",
    "tp_address_1": "123 Elm Boulevard",
    "tp_address_town": "Hilltop",
    "tp_address_postcode": "HT4 5WX",
    "tp_vehicle_reg": "ABC12DEF",
    "tp_insurer": "Zeta Insurance",
    "tp_insurer_polcyno": "POL1098765",
    "tp_phone": "0456789012",
    "tp_mobile": "07456789012"
  },
  {
    "source_id": 6,
    "type": "Taxi",
    "daystohire": 8,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Thomas",
    "client_lastname": "Young",
    "client_address_1": "654 Maple Street",
    "client_address_town": "Greenfield",
    "client_address_postcode": "GF5 6WX",
    "client_vehicle_reg": "DEF34GHI",
    "client_insurer": "Epsilon Insurance",
    "client_insurer_policyno": "POL5678901",
    "client_phone": "0567890123",
    "client_mobile": "07567890123",
    "client_email": "thomas.young@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-10",
    "accident_time": "11:33:44.888Z",
    "accident_location": "321 Birch Road",
    "accident_circs": "Hit and run",
    "tp_firstname": "Ursula",
    "tp_lastname": "Vance",
    "tp_address_1": "987 Pine Avenue",
    "tp_address_town": "Shelbyville",
    "tp_address_postcode": "SH2 3HJ",
    "tp_vehicle_reg": "GHI56JKL",
    "tp_insurer": "Alpha Insurance",
    "tp_insurer_polcyno": "POL2109876",
    "tp_phone": "0789012345",
    "tp_mobile": "07789012345"
  },
  {
    "source_id": 25,
    "type": "Taxi",
    "daystohire": 7,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Ursula",
    "client_lastname": "Vance",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Hilltop",
    "client_address_postcode": "HT1 2CD",
    "client_vehicle_reg": "JKL78MNO",
    "client_insurer": "Gamma Insurance",
    "client_insurer_policyno": "POL7890123",
    "client_phone": "0123456789",
    "client_mobile": "07123456789",
    "client_email": "ursula.vance@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-09",
    "accident_time": "12:44:55.111Z",
    "accident_location": "654 Maple Lane",
    "accident_circs": "Rear-end collision",
    "tp_firstname": "Victor",
    "tp_lastname": "White",
    "tp_address_1": "123 Elm Road",
    "tp_address_town": "Clearwater",
    "tp_address_postcode": "CW4 5WX",
    "tp_vehicle_reg": "MNO90PQR",
    "tp_insurer": "Beta Insurance",
    "tp_insurer_polcyno": "POL4321098",
    "tp_phone": "0345678901",
    "tp_mobile": "07234567890"
  },
  {
    "source_id": 17,
    "type": "Taxi",
    "daystohire": 6,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Victor",
    "client_lastname": "White",
    "client_address_1": "987 Pine Street",
    "client_address_town": "Riverwood",
    "client_address_postcode": "RW2 3HJ",
    "client_vehicle_reg": "PQR12STU",
    "client_insurer": "Delta Insurance",
    "client_insurer_policyno": "POL5678901",
    "client_phone": "0456789012",
    "client_mobile": "07345678901",
    "client_email": "victor.white@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-08",
    "accident_time": "13:55:11.777Z",
    "accident_location": "321 Birch Boulevard",
    "accident_circs": "Side collision",
    "tp_firstname": "Wendy",
    "tp_lastname": "Brown",
    "tp_address_1": "654 Maple Avenue",
    "tp_address_town": "Hilltop",
    "tp_address_postcode": "HT2 3HJ",
    "tp_vehicle_reg": "ST78UVW",
    "tp_insurer": "Gamma Insurance",
    "tp_insurer_polcyno": "POL3210987",
    "tp_phone": "0567890123",
    "tp_mobile": "07567890123"
  },
  {
    "source_id": 10,
    "type": "Taxi",
    "daystohire": 5,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Wendy",
    "client_lastname": "Brown",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Riverside",
    "client_address_postcode": "RS3 4ST",
    "client_vehicle_reg": "UVW12XYZ",
    "client_insurer": "Alpha Insurance",
    "client_insurer_policyno": "POL7890123",
    "client_phone": "0678901234",
    "client_mobile": "07678901234",
    "client_email": "wendy.brown@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-07",
    "accident_time": "14:11:22.888Z",
    "accident_location": "654 Maple Road",
    "accident_circs": "Hit and run",
    "tp_firstname": "Xander",
    "tp_lastname": "Smith",
    "tp_address_1": "987 Pine Lane",
    "tp_address_town": "Clearwater",
    "tp_address_postcode": "CW1 2AB",
    "tp_vehicle_reg": "XYZ56ABC",
    "tp_insurer": "Beta Insurance",
    "tp_insurer_polcyno": "POL4321098",
    "tp_phone": "0789012345",
    "tp_mobile": "07789012345"
  },
  {
    "source_id": 20,
    "type": "Taxi",
    "daystohire": 8,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Xander",
    "client_lastname": "Smith",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Hilltop",
    "client_address_postcode": "HT4 5WX",
    "client_vehicle_reg": "ABC34DEF",
    "client_insurer": "Gamma Insurance",
    "client_insurer_policyno": "POL5432109",
    "client_phone": "0345678901",
    "client_mobile": "07234567890",
    "client_email": "xander.smith@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-06",
    "accident_time": "15:22:33.999Z",
    "accident_location": "654 Maple Avenue",
    "accident_circs": "Rear-end collision",
    "tp_firstname": "Yara",
    "tp_lastname": "Thomas",
    "tp_address_1": "123 Elm Lane",
    "tp_address_town": "Greenfield",
    "tp_address_postcode": "GF2 3HJ",
    "tp_vehicle_reg": "DEF56GHI",
    "tp_insurer": "Delta Insurance",
    "tp_insurer_polcyno": "POL1098765",
    "tp_phone": "0456789012",
    "tp_mobile": "07456789012"
  },
  {
    "source_id": 15,
    "type": "Taxi",
    "daystohire": 9,
    "creditrepair": "Yes",
    "authority_id": 8,
    "client_firstname": "Yara",
    "client_lastname": "Thomas",
    "client_address_1": "987 Pine Street",
    "client_address_town": "Riverside",
    "client_address_postcode": "RS3 4ST",
    "client_vehicle_reg": "GHI78JKL",
    "client_insurer": "Alpha Insurance",
    "client_insurer_policyno": "POL6789012",
    "client_phone": "0567890123",
    "client_mobile": "07567890123",
    "client_email": "yara.thomas@example.com",
    "plate_type": "Private",
    "accident_date": "2024-06-05",
    "accident_time": "16:33:44.444Z",
    "accident_location": "321 Birch Lane",
    "accident_circs": "Side collision",
    "tp_firstname": "Zachary",
    "tp_lastname": "Wright",
    "tp_address_1": "654 Maple Road",
    "tp_address_town": "Hilltop",
    "tp_address_postcode": "HT6 7WX",
    "tp_vehicle_reg": "JKL12MNO",
    "tp_insurer": "Gamma Insurance",
    "tp_insurer_polcyno": "POL3456789",
    "tp_phone": "0678901234",
    "tp_mobile": "07678901234"
  },
  {
    "source_id": 14,
    "type": "Taxi",
    "daystohire": 10,
    "creditrepair": "No",
    "authority_id": 7,
    "client_firstname": "Zachary",
    "client_lastname": "Wright",
    "client_address_1": "321 Birch Street",
    "client_address_town": "Riverwood",
    "client_address_postcode": "RW4 5WX",
    "client_vehicle_reg": "MNO34PQR",
    "client_insurer": "Beta Insurance",
    "client_insurer_policyno": "POL7890123",
    "client_phone": "0789012345",
    "client_mobile": "07789012345",
    "client_email": "zachary.wright@example.com",
    "plate_type": "Commercial",
    "accident_date": "2024-06-04",
    "accident_time": "17:44:55.555Z",
    "accident_location": "654 Maple Boulevard",
    "accident_circs": "Hit and run",
    "tp_firstname": "Alice",
    "tp_lastname": "Johnson",
    "tp_address_1": "123 Elm Road",
    "tp_address_town": "Greenfield",
    "tp_address_postcode": "GF1 2AB",
    "tp_vehicle_reg": "PQR56STU",
    "tp_insurer": "Delta Insurance",
    "tp_insurer_polcyno": "POL3210987",
    "tp_phone": "0123456789",
    "tp_mobile": "07123456789"
  }
]

# The API endpoint and authorization token
url = "http://localhost/api/v1/requests"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAxMDg3ODAsInN1YiI6IjEifQ.KOXSFwOpyxeavuFn8pqym6WbrmxVfEUOxBhmpZ60L-E",
    "Content-Type": "application/json"
}

# Loop through each dictionary in the list and send it as a POST request
for entry in data:
    response = requests.post(url, json=entry, headers=headers)
    print(f"Status Code: {response.status_code}, Response: {response.json()}")