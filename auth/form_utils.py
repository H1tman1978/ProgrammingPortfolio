PHONE_NUMBER_REGEX = u'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
REQUIRED_FIELD = "This field is required."
USERNAME_LENGTH = "Please enter username between 3 and 30 characters long."
PASSWORD_REGEX = u'^(?=.*?[A-Z)(?=.*?[a-z])(?=.*?[0-9])(?=.*?[:punct:])[a-zA-Z0-9:punct:]{10,}'
PASSWORD_REQ_MSG = "Please ensure your password meets all the requirements."
STREET_ADDRESS_LENGTH_MESSAGE = "Street Address must be between 5 and 100 characters long."
STATE_CHOICES = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
    ('AS', 'American Samoa'),
    ('DC', 'District of Colombia'),
    ('FM', 'Federated States of Micronesia'),
    ('GU', 'Guam'),
    ('MH', 'Marshall Islands'),
    ('MP', 'Northern Mariana Islands'),
    ('PW', 'Palau'),
    ('PR', 'Puerto Rico'),
    ('VI', 'Virgin Islands'),
]
ZIPCODE_REGEX = r"\d{5}([ \-]\d{4})?"
STATE_VALIDATOR = ['AL',
                   'AK',
                   'AZ',
                   'AR',
                   'CA',
                   'CO',
                   'CT',
                   'DE',
                   'FL',
                   'GA',
                   'HI',
                   'ID',
                   'IL',
                   'IN',
                   'IA',
                   'KS',
                   'KY',
                   'LA',
                   'ME',
                   'MD',
                   'MA',
                   'MI',
                   'MN',
                   'MS',
                   'MO',
                   'MT',
                   'NE',
                   'NV',
                   'NH',
                   'NJ',
                   'NM',
                   'NY',
                   'NC',
                   'ND',
                   'OH',
                   'OK',
                   'OR',
                   'PA',
                   'RI',
                   'SC',
                   'SD',
                   'TN',
                   'TX',
                   'UT',
                   'VT',
                   'VA',
                   'WA',
                   'WV',
                   'WI',
                   'WY',
                   'AS',
                   'DC',
                   'FM',
                   'GU',
                   'MH',
                   'MP',
                   'PW',
                   'PR',
                   'VI',
                   ]
