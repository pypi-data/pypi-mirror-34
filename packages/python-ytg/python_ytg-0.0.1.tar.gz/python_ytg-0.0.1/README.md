# Python YourTextGuru

Connect to [YourText.Guru](https://yourtext.guru/)'s API, create guides, check your content optimization.  


## Setup  

Simply install `python_ytg` and its dependencies with `pip`:  

    pip install python-ytg  


## Usage

Get your API key from [https://yourtext.guru/profil/api](https://yourtext.guru/profil/api).  

A simple example:  

    import python_ytg as ytg
    from time import sleep

    conn = ytg.Api('My API Key')
    guide_id = conn.create_guide('My Awesome Keyword')

    while(conn.get_guide(guide_id) is None):
        sleep(60)

    print(conn.get_guide(guide_id))

    print(conn.get_scores(guide_id,'My Awesome Content'))

Remember to also check [the API documentation](https://yourtext.guru/profil/api) for more tips!   
