from flask import Flask 
from flask import render_template 
from flask import Response, request, jsonify 
app = Flask(__name__) 

id_count = 31

data = [ 
 {
"id": 1,
"name": "Cafe Grumpy",
"website": "https://cafegrumpy.com/",
 "logo": "https://cdn11.bigcommerce.com/s-c8vytv86xy/images/stencil/789x789/grumpy-logo_275_1509319914__34161.original.png",
 "location": ["Midtown", "Chelsea", "Greenpoint"],
 "rating": 4,
 "about": "Cafe Grumpy, offering rich espresso, creamy flat whites or a simple full-bodied coffee, has well and truly conquered the NYC coffee shop culture with their Greenpoint cafe a prominent feature in HBO series, Girls.",
 "mark_as_deleted": False, 
 },
 {
 "id" : 2,
 "name": "Citizens of Chelsea",
 "website": "https://citizens.coffee/",
 "logo": "https://images.squarespace-cdn.com/content/v1/5b184ce4a9e0286b32a88717/1535133673887-W4NNUAX8A5UCP6UEG1YA/ke17ZwdGBToddI8pDm48kBDbX3r4DPmFI_mpdEbTCXR7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0hGaawTDWlunVGEFKwsEdnGX41pfjC1dvZtDkZRPr9geg6MDmR1mieO0jksx7sXPsA/IMG_5246+%281%29.JPG?format=1500w",
 "location": ["Chelsea"],
 "rating":4,
 "about": "Citizens of Chelsea, Citizens of Gramercy and the recently opened Citizens of Bleecker, offer modern Australian brunch paired with Melbourne-style coffee – think fresh, healthy and inspiring food and self-sourced green coffee beans delicately roasted to optimal sweetness.",
  "mark_as_deleted": False, 
  },
 {
 "id" : 3,
 "name": "Hole in the Wall",
 "website": "https://www.holeinthewallnyc.com/",
 "logo": "https://static1.squarespace.com/static/5cb0e14190f90435d98b7daa/t/5cb0e1a79cabd10001326687/1582748420288/?format=original",
 "location": ["Murray Hill", "Financial District"],
 "rating": 4.5,
 "about" : "Owned by Aussies, this mini-chain brings “the third wave” of coffee culture to 2 locations, with the FiDi cafe doubling as a cocktail bar after dark.",
  "mark_as_deleted": False, 
  },
  {
 "id" : 4,
 "name": "Banter",
 "website": "https://www.banternyc.com/",
 "logo": "https://images.getbento.com/LD1SfLppREODlMwcVyjo_banter-logo1.png",
 "location": ["West Village"],
 "rating": 4.5,
 "about": "In need of a sanctuary from City life? Stop by for a flat white and brunch (think avocado toast and nutella infused fare) in the heart of Greenwich Village.",
  "mark_as_deleted": False, 
  },
   {
 "id" : 5,
 "name": "Bluestone Lane",
 "website": "https://bluestonelane.com/",
 "logo": "https://d25nroq5gtgh8g.cloudfront.net/viceroyhotelsandresorts.com-2345294611/cms/imagepool/5cb9762a3d33d.png",
 "location": ["Midtown", "West Village", "UES", "UWS", "Financial District"],
 "rating": 4,
 "about": "Offering artisanal coffee and food, including their signature avo-smash, Melbourne influenced Bluestone Lane Cafes and Coffee Shops are located all over NYC, Hoboken…and many other locations in the US.",
  "mark_as_deleted": False, 
  },
    {
 "id" : 6,
 "name": "Ruby's Cafe",
 "website": "http://www.rubyscafe.com/",
 "logo": "https://assets.simpleviewinc.com/simpleview/image/upload/c_fit,w_750,h_445/crm/santamonica/Screen-Shot-2019-07-16-at-2.38.06-PM_FBBECEDA-3F0F-4661-AC4D744940AD619F_62adf8f2-2a78-4835-b6844e590b670867.png",
 "location": ["Soho","Murray Hill"],
 "rating": 4,
 "about": "Trailblazers in bringing the Australian coffee culture to NYC since 2003, Ruby’s Cafe offers espresso with a varied menu of locally sourced produce.",
  "mark_as_deleted": False, 
  },
    {
 "id" : 7,
 "name": "Partners Coffee", 
 "website": "https://www.partnerscoffee.com/",
 "logo": "https://cdn.shopify.com/s/files/1/0087/2074/4527/files/logo-blue-cropped_400x.png?v=1553892430",
 "location": ["Williamsburg", "Bushwick", "Flatiron", "West Village", "Midtown"],
 "rating": 4,
 "about": "Formerly Toby’s Estate, this Brooklyn-based, small-batch roaster, who believes that “each coffee can tell a story”, serves their roast in Brooklyn, Manhattan and Queens. They even offer classes to teach coffee lovers the science and art of brewing great coffee.",
  "mark_as_deleted": False, 
  },
     {
 "id" : 8, 
 "name": "Wattle Cafe",
 "website": "https://www.wattlecafe.com/",
 "logo": "https://static.wixstatic.com/media/c31574_68eeb77d109247859e0999a92b1e63b8~mv2.png/v1/fill/w_230,h_140,al_c,q_85/c31574_68eeb77d109247859e0999a92b1e63b8~mv2.webp",
 "location": ["East Village", "Murray Hill", "Midtown"],
 "rating": 4,
 "about": "Now with four locations in Manhattan, you’re never far from this Australian-inspired home away from home…and home of the *world famous* cacao waffle avocado smash. Guided by her passion for wellness, Aussie-entrepreneur Ana Ivkosic fuses together great coffee and healthy food.  ",
  "mark_as_deleted": False, 
  },
      {
 "id" : 9, 
 "name": "Black Fox Coffee",
 "website": "https://www.blackfoxcoffee.com/",
 "logo": "https://static1.squarespace.com/static/595176f6725e259cb9d64288/t/596e06c259cc68a2a9568fa3/1581713638167/?format=1500w",
 "location": ["Financial District"],
 "rating": 4,
 "about": "With a combination of Australian DNA and first-hand experience of the Aussie cafe culture, the founders of Black Fox Coffee Co bring the joy and craft of exceptional coffee to NYC.",
  "mark_as_deleted": False, 
  },
       {
 "id" : 10,
 "name": "Boundless Plains Espresso",
 "website": "https://www.boundlessplainsnyc.com/",
 "logo": "https://i2.wp.com/aucommunity.org/wp-content/uploads/2017/12/th.jpg?resize=474%2C237&ssl=1",
 "location": ["Financial District"],
 "rating": 4,
 "about": "Melbourne coffee culture comes to FiDi, in this female-owned light and airy cafe along with a selection of light meals (yes this includes avocado toast) and treats. Read the inspiring story of how founder, Jo Black brought her love of food and coffee to NYC.",
  "mark_as_deleted": False, 
  },
        {
 "id" : 11,
 "name": "Charley St",
 "website": "http://www.charleyst.com/",
 "logo": "https://img2.domino.com/dom/image/upload/c_limit,q_auto:best,dpr_auto,w_1200,h_1000/i/082918_CG_CharleyStreet_HT_WEB-12.jpg",
 "location": ["NoLita"],
 "rating": 4.5,
 "about": "Fresh food, colorful bowls and premium coffee. Charley St offers healthy meals for busy individuals using sustainable, ethical and locally sourced ingredients.",
  "mark_as_deleted": False, 
  },
         {
 "id" : 12, 
 "name": "Happy Bones NYC",
 "website": "https://www.happybonesnyc.com/",
 "logo": "https://static1.squarespace.com/static/57e443bc414fb5b51697379a/t/57e939e7e58c62bf312540ef/1579209298780/?format=1500w",
 "location": ["NoLita"],
 "rating": 4,
 "about": "This minimalist coffee shop brings New Zealand’s thriving espresso culture to Manhattan.",
  "mark_as_deleted": False, 
  },
          {
 "id" : 13,
 "name": "Laughing Man Cafe",
 "website": "https://www.laughingmancafe.com/#visit-our-cafe",
 "logo": "https://images.getbento.com/qCUnSMESXi2s3eYBVcH0_Laughing%20Man%20logo.png?w=1200&fit=fill&auto=compress,format&h=600&bg=EDEDF1&pad=100",
 "location": ["TriBeCa"],
 "rating": 4.5,
 "about": "For ethically sourced coffee, check out Laughing Man Coffee, at 2 stylish locations, both in TriBeCa.",
  "mark_as_deleted": False, 
  },
          {
 "id" : 14,  
 "name": "Supermoon Bakehouse",
 "website": "https://www.supermoonbakehouse.com/",
 "logo": "https://images.squarespace-cdn.com/content/v1/599af472e6f2e19ff04ad85f/1569338030864-HITOADLE152PBH5RN60U/ke17ZwdGBToddI8pDm48kL3jzEGkqFlO05Aa_jjDyucUqsxRUqqbr1mOJYKfIPR7LoDQ9mXPOjoJoqy81S2I8N_N4V1vUb5AoIIIbLZhVYwL8IeDg6_3B-BRuF4nNrNcQkVuAT7tdErd0wQFEGFSnAkDVU8phWh555zRPiyuEuAMCWRDvkgohEWLoDack9cSt8uNkUZ3t42Fp5QzamcyPw/sm2.png?format=1500w",
 "location": ["LES"],
 "rating": 4,
 "about": "There’s cold brew and lattes but let’s be honest: what you’ve really come for are the irresistible, must-see-to-be-believed, “mind-blowing”, “bad***” and “f****** delicious” works of art. You’re in the neighborhood on a coffee run anyway right? Almost too good to eat. Almost.",
  "mark_as_deleted": False, 
  },
           {
 "id" : 15,
 "name": "Tulo House",
 "website": "https://tulohouse.com/",
 "logo": "https://static1.squarespace.com/static/5b6724b1a9e02808a74d2a92/t/5dc1d52d2d63854a02feb557/1582242116195/?format=1500w",
 "location": ["NoLita"],
 "rating": 3.5,
 "about": "Opening soon in Mulberry Street is Tulo House, founded by Aussie health coach, Laura Hopkins. Tulo House will offer in-house blended nut milks along with vegetarian, vegan, paleo and gluten-free treats.",
  "mark_as_deleted": False, 
  },
 {
  "id" : 16,
 "name": "Two Hands NYC", 
 "website": "https://www.twohandsnyc.com/",
 "logo": "https://images.getbento.com/ZfVqVYopSlikjHpycQ3Q_twohands_Black.png?w=1200&fit=fill&auto=compress,format&h=600&bg=EDEDF1&pad=100",
 "location": ["NoLita","TriBeCa"],
 "rating": 3.5,
 "about": "Community-focussed cafe, inspired by Australia’s modern culinary scene and laidback beach lifestyle…the perfect place to escape from the daily grind.",
  "mark_as_deleted": False, 
  },
 {
   "id" : 17, 
 "name": "Coco and Cru",
 "website": "https://www.cocoandcru.com/",
 "logo": "https://images.getbento.com/accounts/43857889fb215e92a211902b9e35eab9/media/images/40964Coco_Logo_Circle_yellow1.png",
 "location": ["West Village"],
 "rating": 4,
 "about": "A taste of Sydney in NYC with an extensive menu of fresh, simple food and a range of coffees.",
  "mark_as_deleted": False, 
  },
  {
   "id" : 18,
 "name": "Merriweather NYC",
 "website": "http://www.merriweathernyc.com/",
 "logo": "https://static1.squarespace.com/static/5778125f6a49632d6e73f665/t/577acb5a20099e9ea59c5896/1560364250663/?format=1500w",
 "location": ["West Village"],
 "rating": 4,
 "about": "In this bright modern space, inspired by Sydney beach cafes, sit back, think of Merewether Beach and savour a cup of coffee, crafted by their talented and passionate baristas.",
  "mark_as_deleted": False, 
  },
   {
   "id" : 19, 
 "name": "Saltwater NYC",
 "website": "https://www.saltwaternyc.com/",
 "logo": "https://cdn.shopify.com/s/files/1/0084/6885/6912/files/Saltwater_-_Green_Logo_only_500x.jpg?v=1550790594",
 "location": ["East Village"],
 "rating": 4.5,
 "about": "This homey coffee shop serves Sydney-sourced coffee, and brings “coffee as a way of life” to the East Village.",
  "mark_as_deleted": False, 
  },
    {
   "id" : 20,
 "name": "Three Seat Espresso",
 "website": "http://threeseatespresso.com/",
 "logo": "https://s3.amazonaws.com/threeseatespresso.com/site/images/brand.png ",
 "location": ["East Village"],
 "rating": 4.5,
 "about": "After you’ve enjoyed a coffee and a light meal (yes there’s avocado toast), treat yourself to a haircut, with services available for men, women and children.",
  "mark_as_deleted": False, 
  },
     {
   "id" : 21,
 "name": "Bourke St Bakery",
 "website": "https://www.bourkestreetbakery.com/?fbclid=IwAR2uprOLryWNpY7SwcVop0E8MWyscVtp0Uke-Duz8KZrgR4gsAouLUXoXGM",
 "logo": "https://static1.squarespace.com/static/5a7b32ea64b05f5b71fb566d/t/5aa189e18165f5eecd4c8fc6/1582580001182/?format=1500w",
 "location": ["Midtown"],
 "rating": 4.5,
 "about": "This much-loved Sydney chain opened its doors in NoMad in May 2019. There’s a 50-seat bakery and restaurant, open all day serving up signature favorites including sausage rolls, sourdough, tarts alongside some specially crafted New York-centric baked goods – think peanut butter and jam pastries and maple bacon danishes. Undoubtedly one of the most anticipated openings of the year in New York and rightly so. Welcome to New York, Bourke St Bakery.",
  "mark_as_deleted": False, 
  },
      {
   "id" : 22,
 "name": "Clovelly NYC",
 "website": "https://clovellynyc.com/",
 "logo": "https://img1.wsimg.com/isteam/ip/d726cfa6-72d0-438d-9c44-51db77ea8c9a/logo/a7c06d78-3cd7-4e24-ac4c-bc43d5a7d6bb.jpg/:/rs=h:160/qt=q:95",
 "location": ["Midtown"],
 "rating": 5,
 "about": "These new kids on the block opened August 2019 in Manhattan’s newest west side nabe, Hudson Yards. Named after Aussie founder, Eliot Ritchie, a Sydney ‘burb and how Aussies feel about coffee, Clovelly Coffee is set to become a home away from home.",
  "mark_as_deleted": False, 
  },
      { 
   "id" : 23,
 "name": "Little Collins NYC",
 "website": "http://www.littlecollinsnyc.com/",
 "logo": "https://static1.squarespace.com/static/5a7b32ea64b05f5b71fb566d/t/5aa189e18165f5eecd4c8fc6/1582580001182/?format=1500w",
 "location": ["Midtown"],
 "rating": 4.5,
 "about": "The bustling energy of Little Collins cafe reflects the spirit of its Melbourne street namesake.",
  "mark_as_deleted": False, 
  },
       {
   "id" : 24,
 "name": "St Kilda Coffee", 
 "website": "https://www.stkildacoffee.com/",
 "logo": "https://static.wixstatic.com/media/418ed8_94fc7b3bc5254a0a92ca29910a6db7b5~mv2.png/v1/fill/w_102,h_102,al_c,q_85,usm_0.66_1.00_0.01/418ed8_94fc7b3bc5254a0a92ca29910a6db7b5~mv2.webp",
 "location": ["Midtown"],
 "rating": 4.5,
 "about": "An Aussie multi-roaster cafe offering seasonal single origin coffee for Espresso, Filter and Cold Brew plus an assortment of pastries from Manhattan bakeries.",
  "mark_as_deleted": False, 
  },
        {
   "id" : 25,
 "name": "Hutch and Waldo",
 "website": "https://www.hutchandwaldo.cafe/",
 "logo": "https://static1.squarespace.com/static/5ac3793cf407b411e9652400/t/5c080c824fa51abae3708b52/1581624082788/?format=1500w",
 "location": ["UES"],
 "rating": 4,
 "about": "Sydney + Melbourne founders offer spectacular coffee and food for the soul, and are on a mission to be part of the solution to eliminate plastic waste in the world, such as encouraging guests to BYO cup.",
  "mark_as_deleted": False, 
  },
         {
   "id" : 26,
   "name": "Abbotsford Road",
 "website": "https://abbotsfordroad.com/",
 "logo": "https://abbotsfordroad.com/wp-content/themes/abbotsfordroad/images/logo-with-tagline.svg",
 "location": ["Gowanus"],
 "rating": 4.5,
 "about": "Brooklyn roasted Abbotsford Road Coffee can be enjoyed at their HQ and Cafe. They also offer in-house training for coffee enthusiasts, from novice to professional barista.",
  "mark_as_deleted": False, 
  },
          {
   "id" : 27,
   "name": "Brunswick Cafe",
 "website": "http://www.brunswickcafe.com/",
 "logo": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMWFhUXFxcXGBYYGBgYGxgYFxgXFxcaGBoaHSggGB0lGx0YITEhJSkrLi4uFx8zODMtNygtLysBCgoKDg0OGxAQGi8lICUtLS0tLS0tLS0tLS0tLSstLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIALcBEwMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAEBQMGAAIHAQj/xABIEAACAQIEAwUFBQUGAwcFAAABAhEAAwQSITEFQVEGEyJhcYGRobHBByMyQtEUUmLh8CRDcoKSslOisxUzY3PC0vElNGSDo//EABgBAAMBAQAAAAAAAAAAAAAAAAABAgME/8QALBEAAgICAgECBQQCAwAAAAAAAAECEQMhEjFBE1EEIjJh8IGRoeGxwVJx0f/aAAwDAQACEQMRAD8A4uKLtXPDpv8AOhG3qUAiJBGgPsOoPpTsC69le09o2LmDxaF0InDuPxWbp03kfdmZPSD10G4mptu1t9R15EHZh/XWqorQwI060+vXjInUBAIPTWndktGi391Oo+YpzwLAWL1oWnLBrcwVI1RnZhuDsSf6NVPFjYqT6VLh8fcshbtswyll1EghoMEcx+lAHTeG9g84ItXl15OI+Kz8q2HYDiOGc3Ew9u+pUoQtxdVMT+LKeXQ1TOE/aLirJHhtvHkyn3g/Sr3wf7cEAC38LcHnbdW+DZfnU/ctTaVUJsZZyH+0cPxVkj8yBnX3sMtC4e7hWP3eLykcrilf+YQtdL4f9rXDLkZrr2if+JbYR6lQyj306OL4VjRGbB4g9CbTt8fEKpKyHJI5fa/aom1cW6I/K6uPjUOMxUmMRhUYdSkfGIq94z7POGuxZbT2m62rjrHoCSo91LcX2Hu2x/ZuIXf8N9FufHl/ppuDQKaZzrtBhsP3Au2EZD3gQgsSNULaAn0qsE9RXRuO9nOIXbeQrYcB882zkYkArqGgbHlVIx3B79o/eWXX/KY940qaYwBrSxNQtZ6GigugrQrSAFKkVrnooitCtAyEPXs161oVobXQ0Ab15WoDQdJrTveooAkmsmo++FZ3goA3mvCa1mvJoA2mvM1azWUAbVoRWTWTQBqRXhr0mtaAPIrKysoA8rKysoAlbc10ZOB28Tg7AOji0mVxuDlGh6ieVc6I0Nd1xHZO5h7Vt7I/u0Ny2dicok6aAzPiGh59RSWhM4tjsDcsOUuLDD3EdVPMUbh73eAg/iC7dYnUe+r/AMSwFrFWyriCPY9tv69hFc64nw25hrmV/wDK42YeX1FICPEJ+H1rW+R3bA+RHsmtnuhsvWdfcahxf4faKBGvD8G9wwqlojYTEzHyPup/huBja4sEeo+VbdgMMXxIURtO4GgBH1q58SwL27twOpWSCJ5iNx1FJFFTfszaOzOPcR8qDxHZU8nB9Vj4yatXdCdtfWKw0xFVwuGx2HINq7cUAgxbuso0PSQKulntXjE/vc3k6qfjE/GgyKjNugKQ5t9tLv57aH/CSvzmp07XYd9Llt18xBH6/CqvdtUI60WDii4X7uDuwC1lhA1cANrJIJYb60DiuyuHYFlEeaNPw1FVdxUAYrqpI9DHypBsOxXZxROW4f8AMv1B+lL7vAbo2yt6H9YqUcSujTOT6w3zrdeNONwp+FACe9g3XdSPZ9aHK07/AO0hMwR6GakOLtOPFE/xAfOkMr0aH2Vu80+w/D7ThjoFESytJ56KswSfpyqNODq50YqCecGPXaaaARLbBOoHuFDtaFXTE9i7ia96pGWZgjcaDnSHE8HuKY0NACY2/OtdaOuYVxup+fyqArQBCzV6oJq52fs+xdzCW8YgR0dSRbzZXABKg6wpmJ351XMVgntmHRkOsZgRMbx19lYrPCTcYtWjT0pVbWhcRWs0fYwzOyoil3YwqqCSx6ADU0/7Q9jDgsMtzFMBfumEsqQcgAzO1w7EgQIGgLDU0SzRi1F9voFjbuioTWTRV/hd1dSpjqNflQbAitjM2rytM1eg0Ae1lZWUAHWknSvsdbAKKCNlHqNOVfH/AAxZuKOrD519jrWj+hf9/wDg/Bzrtl2aQMHRglxpybDNGpGXnvqNuYynWqFxC0twGzfSD09PzIfL3ieh1vH22A91hypIIZzI3H/dgEe00g7fYYW7qWwpbNbZ99VKkDwnfn8DU+COmco4twp8O2uqn8L9fI9DS7EPI9tWzHcRUTbuDMCOYgkfxDkdNx0qrcQtBTKmV5dR5GkMbdinAxuHLGBmaT0+7cD4xXR+NYxQwVn3nKCZ8yBXLOCki4kb6/FSD8DVn7O27l+/aR3Jyl4J1/u20+FNAxsz1G51o3GWch1oU660CPAK3s25NYor1FPKkykT8T4a1sAsIzCR5g60ivLTzimMdhbUrlCIE05xMsfMkz/QpLeeojdbKlVgVxa9XCkjatmcU97PY+3lvBwvhss4LGJYFQFGmpM/XYGlNtLQ4JN7KnftxQzCj8digxkCKEWJ1pp6E0r0QMtQsKt+G4TbbDm5nXSBEiZMkCPYfcelVjEqAdKmM+TKlDirAwPfU1nEOplWI9v02rfDWCxAFS8RwTWgSRyJ+FVyV0TwbVhbdqsVGVnDCZ8Sj5rGlRN2jc7ovs/nNdL4/wBmMLZs2LaWVgqzMWAZmY5dSx1+g5Vy3tHglt3yqLlXKpgTud96omjLvFc2/wAhURuB4AgsSAJ2k6Df1oJLRJgCTTLDcPdSriCymQp2nlr6wfZWc5JFwi2zpPEe04Szaw6aIipbEfuqANB6V2P9iwzYcIUtPh8ggMFZCsbmdDprNfJGLuXQ83Mwfz00PTy9K3t8XuqmQXGyfuEkr/pOlcvwvwiwptbb7Z0fE/Eeo1FKkvB3W1h8Fhr9x8FZRM2mdZM9chJOVSeSwDFcr+0HHnE4piWGW2ptqJ5/nOnU6eiikNjtLftnwOVHQbe4zUdq6z/3bev/AM71ng+ClDPLNJ2319vzoeX4iMsahFV7jG3xI80P+Xxfoa8N+y4AYLMbEQfjFCDSm/Cbr32Wz3Pek6AACfbOgHmSK7nNLbOXi/BVOIW1Fxgv4QdKHyV0HGdlrOd0ZCrrocpiDJ9h5VWr/BBJCsdDz/lV8lVip3QhyVlMzwe55e/+VZRaCmS8JE3bY/jX/cK+xq+POCNF60f/ABLf+4V9h1b+lfnsHg519sQ+7serf77Apb9qNsDGWCP+DcPvdad/apbzLYHUn/rYb6TSb7Sl/ttlTsLDR7X/AJCmvBm/z9jmfaHDg3E0/L9XqtcXs5QPX6GrfxxIu2/8J/8AVVe7TL4E/wAf0NOSJiyDs/HfJPn8qd2LrWwt22fEHaD/APrc+0Uq7L8PW/f7tnyDu3OaJgqARI3K9Ypolt0my6zBuEMviDTauRBGhB1M+R2ipTLaLh2We5iAbj5Tq6lAJmEnUHffbyoVrKySIEkmBsJM6DkPKpeB8PH7Dev28U1u7azXFRCkmNJIPigQNRH4t6lw/BTll7zA67qN/YaHplLapALW4rxCQfDvUzcPYmBcn/Kfnmrw8Oug6XLcjbVh9IqW0NRZJ2hxeZlAXQIk+Er4soz6dM01W7zVZONYXFXXLBBlMQA4aIEanToTSK5w67MDIT0DAf7oqY0kOVtm/Brdt7qI4JzsqaRuxAHxNCcct2hcZbZ0BI5cjHLSmOIsn9nC9xN3OQcpzeHKuUysgksWEAz4ar12y4PituPVW/SktuynpURi1JiieJ8JeyqsxU5hmEGdKnxncDDo4J7xmZSDGmUKZiZg5tDHI9KV3sU13IHbRFFtdhlQEsBoOrMfaaLbCktGJj7otNZDfduyuywNWUEKZ30k+81DdwdwKGKmDzovivDu5yeNSWVXEfusJU+0UTZxl/E27WGUHwFzMznzRAjllA+J8oTlq10Cjun2J8NjHtmVjMNpEiaP7XcY/aLlx0DC0R4FYKCBlAMhdN5OnWgMbaNliHiRuKY47Frdw9lEsqr+MXCVI5gIQSfFImYGlDSbTSBNpNNnYO141sj+D9K512tS0GsoADcuzLTOQBgvjA1XQg+mtdH7W/jtjon1Nc24lZU4m4ZAOhPUhVFXONkwlQDa4Wbb90EbvJyxEsSdgAN55RvXSeB/ZZcay1y/c7u6VlLYg5TGneH6Dbz2qi4btGLWR1Jz2gMrkAkAGVAPQfKnvE/tTxmMsth7YtWCylWuAtmIOhCf8MnXXU9IOtccMbk2si/s6ZZFBJwf9Fc7TYm3jsIt5Mvf4cQwGma1z06KfEPImq3w7hJugMQVUTP8XSJ2p5wjszdtvnZlXKNWDQoUiTJ5iKI4rxgZRaw4EDTPlgn/AAjcDzOvpWuHF6MeC68fb7EZcnrPlVPyCWODLbXMVVf4mP1NT8O/ZHLW7tw5mHgZJOUidD+VgfpSw8Oa54nYljzJk+8mjuFcGUEkiSDpOtaZIucWk6MoSUZJtWPexnYZMXeZbuJRLaQSAR3lwfwBtFHUmY6c6f8AbdMHhTYtcORQ9vN3lxGBB2gXH1Ltv1jbSar1vBcopjjez11BDDLOxGoPoRpXLmnjxY6zO7/k6sKnkyXh1QFh8S112JYZzEjQnSap3FcRdQnLr4jPhmnl7gzl8qIzNqQFBJ01Jga6daZYPswgwty/dvS4QlLSxof42Op9B7zUQ+LxQhFeOkVl+GyObf7nPTxa71H+kV5Vi7jyrK7OSOTixHwtZu2h1uWx72Ar7Cw5kV8jdnB/asPP/Hs/9Ra+vVUDatq0ZVuyi/afP9njqR772FFI/tMeeIWx0ww+Ny5+lOPtReLmD82I/wD74SkP2kP/APU/TDW/+pdprwJ/n7FM46PvbQ8j9arfapYVP8f0NWjjRm5aHPl6a/Wq92w/DbB3z/Q1cvJETbsXw0XsSymP+4vMJ/eUAj6034RdtYZRcvJce04a2y22Ct4rZ1GbQ7bGOvKk/ZRyt8kaEW7nyApnxm6EwVtygf70CCSN7bCZGoNRScdl3TNbSnuhcCP+zuzKhaCwIZYW5l0BlQRyPLaum8ZwvdpnGznUz7apvZvBG5g7DeIBnueGSQQGBIjY6irt20uC3bNpi6ozQCFBgj91ipEmdqjJ8qRcVbe6K7iMSiQwIkiekDqRSzH8bSNAGHUA6ct/WmHH8FbUYa+cuW0VQrkWbupb7zUFpAiRVdxHD1VLw2F4gp4CotkEkhQLhzaaa9KycrNVfuHYXHhiIMaiBXrjVtY1/Qf1PuFLHOe5aClBkVVaJBYyJJmYEyfbzpw9wePTfXpR2hpgd58vUxOoJ0byjnPyoNiee4jWR8+fPWvX9ojoRGp6RpUTuD4SefSfQTRRQx7OHNcIcSI2Oo+NP7vCsM34sPZJ692oPvAqt8GukFyNITT3gUp4p2pxth8rd2ynVWKHUexhqOY/WrjRnO+y3Yrs7hH/ABWtgAIdxAGgAhtABypDxjsubbI+ERmgzCM73Ay6ghImBvInzjmmTt/f/NbtH0zL9TU1v7QXBDdwAw5rcII9DlonFtUnRMWk9odYPs42EUXryKLouBBb0dhmUt498voNp1it/wDsMBDcyl2AJAYwJGvLelWF7Vpec5rVwSQzHOCNOZkan46muh2UDIo/e09+lPHBq7dkzlfRP2sb71f8A/3NVExPBkz4nEyxY2n0lYGgXRQCToBqSN9qvPakfff5R8zVMxd895fUgADDPBhQSDcUb7nWd+lWJeCngSp0/qffWvD8d3TExJ2E8vWiHcZSIP8ARo29j8K+DFl8JGKVmIxKsFlS0hWWPHAhR0AkGZBybNVGyPE9ozcTu2QGDM+IGeU+Igx6UThMMBb7wKWMZoG50OgpRw/hly8WW0MzKrOVEk5UEsdo0FXDg+B72ytvLnDWtVmJGSTry0mhUJpiS1xJQBntsnmzWl+DODRFjj2FtzL78lUt8Rp8aXcY4WthQRbtbiRkmJXMRJOoG06Uut8MzqXyALI5xAJ3PQaHkZiOdX0RVllsdrLTtlt2nMCSzZVAHUwSfhrVps4y9mVmeQpBVSJBA2zA7+lc2VVVQifhmSTux/eb6Dl766PGg9BWU8WPK1yV10aRyTxp8X2PG7RHu2W1ZtWc4IdkGpHQE7Dy5TpXPLbtBEmOlWi0hIMCYBqs2WGuvsqcsIcUqKxTlbdkXdVlEGK8qLLoqvZ7/wC6w/8A59ny/vF58q+p348iglrdwKDGaBBOsfmnl0r5PwV/u7iXInI6PEkTkYNEjUbV0VPtZuOCGwVsruB3l4gkSOmnOu+LjVM4pctcS+faJiFunBMoPiYROhE4rBr+tJPtKP8A9Tj/APGt/wC+5Q/Fe0zvYt324fbY2wCqd7eBUB0IAC7nOtsxHSpLD3+Kt39zCNhrygocwvHNbUBl8JXTxMwmNdddKK2D6Kjxa597a8gfpSztqwa3ZbnnIP8Apq98S7CXSyP+0YdYlYZmUk6bArrr8xVZ7a9kcSndL925zOfC+4WAT4gJ3G1OXTJiKOzKfeMf/Cf6VdODWrJw9rvrS3VV7xKNMNmwxAnrGsdCZ5Cq52dwpUvI1FpwfWBV6+z6yDcwwIkF3BHKDh7h+YFTvi6NE6kGcGxtu7ZsILZthS8AKFXw28ihRvsF15npRn2mcQtW1S1eRnQ/elVLiMpgGVZeh0qLG4bucQq5cga7d7sRlkZgBl6gAjbqKffaHwfvsJcYQXRWIJ/dI8Q3Gnr0qZp0rLjK5N9HO7uKs40WrKd5k/HbWXSc2k5T+LXTnrtSrH27jzacPGFV2hWIygsSS0rJ1POrTwHAWLGGRrZw94K3hvgAuFdiR4tfEGI05CRyqPH8JQM5Fq0O8BzkKAXnU5jzkgbztWTxtGin9yn3Je5ZvMGlwiqYADKrKsjQZjvJozuzlJ5enWJ2/rWjjwuGteAAIfDA0EtJgchJ5c6XPdlTrEztPTzo4tDsgdxqoGnprPKg7nOBMH+hRxU9D667daHuNAPWdee2mn9dKKE2bcKOl3T8o/3CoeJYVbqFG9QeYPIij+D4fOXUQCV5/wCIVNf4S45r7z+lKSfaNcU4cWpHL8bhWtOUbcc+RHIitcPYLtA9p5AdTV84p2ea6sEqGH4W10Pu2NA2+zF1FyqU8zJlj1OnuHL31d6OeUUnp6FdhAoyrt8Sep/rSuu4F9bY/iQf8wrnCdn70/k/1fyrovDh47X+NP8AeKI2TOvAw7RlO+AYkaDNEbRIjzma5fxriQtXb5JLZ0NoLliPEG0bNrqp5Dn7ei9p3/tDei/7RXJ7uLf9sxIADDMdWMBADqZ5fypvRUd0Qrig4kbwBrE6QOXlUF+5znlr6CiMWoUGTLTrpGnWgDe1B6QfcahbKej2zf1OVjqNYJGh+lXOzjjZw4uAwURT7IEj2iRVb4jgL2U3TbIAALMcs5fSZ57U3xOLuWbKK9oB7gDI2cEBViCAOZkaEU0myZOuhPxjjb3Y0y7GVY6+HKI2jSo8IbpUo2dpIIGpOk8vbTrD4KzeUO12zYdWnxvc1KgEMZOmvrt7Kkx3AS3DhxM4lw1xiO6UEAeMiJDa+6m1ZMZbFSYK5IHdvuPyt+ldAZ9N9q5Xw7EMl5SHYBhrLFZ3HI1M6pnuK34QGKfmExIGp61KtFPZ0e7iUQDM0Z1lY1B0quYY7/11pNY4teuRnIhQAsKFgdB5UzwtzQzUyuyo1QWza1lQM9ZWdGllatW9RpOo06+VWRw1tzFq6yMZPheAHUHKDroNPj7VXB7c3rQy5vvbfhic3jXSOc7RX0HgcJdXVbKYdNzFpEJPIAAZvj1rsSOYpH2f23vYq2gTEJbU94xe04UspDRngAS3WSZO9PUw7JjFZ3K2/wC0ZYZiBD3DbidRlJI9pG0U6CP3yXDfu+AtpMqcwAMqTBiNOmY0fxfs4MSLZW7kCHMMqDxayQ0nY9BFOTEvcY8TsW7toC6gdZBysAfeCIriq3Ln7QEVzIuEHlFsMhkxAgREbGYIM12FuGXGA++IIPJAJ8jr6e6qw/2ap3rXf2m54gRkyrk18tzz3PM0mt6EnRz7srxW6uJYdy8BWUg2DdZ0J8SkGNI/Nr7ZNdSwHH8JYFx0w2JtKxDNNh1VYEbbKIqvcX77Bs9rD3JcKCGeQJInWOQpLx6811CbtxmZVJHiMZsrDQSBGu223SplLwWkdCPGrN7usSpbu4JRm7vK0jNmAIJGgiRH4qQ4vtvhsa7WRd7vBhZvXzNsMW0WyrGMv5izaHwwN5rglk3WyiWfu4yKzkhY2ygmBqI06Uz4vxrE4gLh3S3b7y4mUIBbQmBb8QWRH4TPlVKidnR/+z7GIx6tw/FratO6i4LZDW2g7BAcslYUSNzPr1XHWLKwGtqZPJJjzMDQeZriXYHhK8Nxr3MTfsE2wFCLcGVyyq6vmcAkKDpA3J169Vw/bLD3kuMLlgLbCl2N9IXMTlkxpJFCe9BJWibF8PtHZE9wquX+BWU1Fm2AP4BXq9r7OHsWVvXrNxyihr3foBcdVXORCwdSDH8Q60LxDtthFdkL2wV0INwSCB4gRlOxn3VbcX2Z1JdE1nh9l1zdykbTkHLcHShMTwazGYW0IHMKDr7Na1bj1he7JxFtReyMgNwnMCSs5coA1WPPSirtu2g8GMRgwNxBmVgwnVkAbxAaiRtrUX9i6fuJlw4tmbeVAeYUaD0Ak+gofG98Fzpct3V2m2yEgiN1aGG45aSK24L2zQXbtrLaY5XtgFH1IaBE6Rz9lD8Kv2Ee6Tkud5auFWcNb7tnu27G5zQc6jX0qXFPoabXYEuOY/icKehVTt1IBFEi64RyTLeHKMqAGZkmV5aEUldoZ7ZyE5nB3YyPCTlDrmEjy9aGXFq4Je7kaY2YiEJRZALH8OXrz9ay4v7fsaWvxjZMTeJganyVDp7BTPg/Est23naQGBIA5AzoAPSlnDe02ItJ+zpldBmAKHUZoYkHLrEk69fKveA8QtW72WSjFCodspCr4SVMTzA1jlT3Hf8AoWpOv9/0Nu0HG7LX2YN+7odDooGxqicZsWmLBLkd4zPcMrMk/h35dfOrbj8FZu3Z75WuQSCsMCAqg7QNo3pJiexiEllCsSSTrzPt0rOWZXT/AMG8cLrX+RRxHDKQzLPdk+An8qgnQnYnnQZwqZ5EqBtOvy1psezrICBbMHcDMQfUCRUN3h4OjKfT+VL1UNYWj0cQYAqHDK2hVp0OxAPT1rziuJN118OTIiplnMNJMg+YioH4cjaQB5lQT79KhtYcpoCCAekfrWkMiM8mOXsD4x4BFObeK4hd4cmHFpGwwMhwAHUSXyzmEjUn8JOtB2+H2nVjcusjycoCyCIETpoZmiOznGHsYe9Ze1cbMQVKwQsLBBk7aDar5LwzJRa8FXv2yHgyIkdCNJ9lEW7jWiRIO0kw3s1JHuou9aUqfumVtDLOp965AY9tergLLBc964rn920rD2N30/8AL7KGrWwjkcHcXTIrdu4rxlDErn0hhlOs6aD6VEmCvF84C7zshA84PSsu4W8IBV9JggGYPpyrx8Q1sgZgWgFtGBUn8pkCSBEkaUq9i+bapssVuQACZManrWUDgu0ltUVXw2dhu2eJ16RpWUuAuYf2QuhcZhidu/s/9Ra+h+L8VsuTbS6zsDqlhe9cHoxAK2/V4FfOd7D27F+1L97bDozHIVzKrguMrHUEdYmauPaD7XroQ28DYSwgByswBaI/Kg8Cf81bxkuJnNPo6ddGppnwi+VEcqq+C4mXAz78zVh4a0ioUlLobi12PyJ1FZFQ2Wipwaok5B9pHFRaxdxQCzBUMDkCg1PTn/Oqngr7X7V6ZzlWCgAk/hO3tpz9qZT/ALQvZv3bZIB1ICLE/ujzPsG5BXZfCriFXIAdcuUMApmQZB0bfnNc97/U6EvlOT8S4ZcDPcRTkRmhuiqYDA8xtr50XhMOlzF4ZL2ZUKLmyxm2YiM0ASQBrXXeJdl+6i3nCLpK98znTYsAQY2MbSB0FQdkuBi1eN23ZLXLeQJdCKWXPbOYfeXwNmOuszOlbWZUIeJdmf2u6xsXgoRLNvKyhiQtlVkm2Ss+HYdeURTLhnYlsPZvW8Tmu98bJCp4SBaLtJzMpHiK8+VXbg1xjicVnLqzLYY5ioLSLi65CV/LET0pvnUHUjXmZ/o1O1semcs4x2NS5bsohbDi211zmi4fvBZGo7wn+721GhorH8Iwyord01245ckgABiWJJ1UkbwPID1rouKvW4EFfOAf/VSXGY1SToDlA0AG2p5ga/1NS2x0ipYfg9p7llXsOoyDK05zafvFCrkhcyDMWmRGuh2ovheCs92ndA3FSx3Kh7cBg3eMvizEr5kb9eVNMPjm71FKSpcQQWEDw+InLlkNm8PMc5pbwfHvZGTunygKkfd2wF5t+NjAFWmvchpldxOGfLnSyqasQQuqkG0VBYzuDcHnFb8He+AWy20dVtqxKoFKl2Zjl/DrB0jc7UXibza6yCDEGVjrpM8vLQUGt51bOrNIAkQdhm1j83pUxlsqUdBGUh+8RkjvcT4AQDmN5wh0ExGnPQ0DiLD3rS3CLWfKhLZAM0F+8MAQSZTpsajtYkMXBZl8Vw5srkAm6Y5efmd9KzHWIZAS7MqpLB/CdzJIYA79Na0MwF8HHeGQ8SFVMyFYIEEhRqdYIJj2V62KNxraMXhrlwrInQMsBiYKjLI2NE3mtjvGIY5yfCMucHPM7kER5jzioBbIe0bRDQGOvhOrGRGoBj5iKQxrcwiW8XcgAQGC/wDJMf1zr2+/VQT7j8Kxrd27iLhZQriSyTI1IHhbY7CtWsMpEyvy99cmeuR2fD24mG+RzdfXxAe+ve/ZtCEf10PuP6Vq7MsbH16dDyrW0yNIJykaAn5E9K5qVWdGzV1t87cctP5R8qFucNssZDQfP+hRaJALDUHTfUfqPWtLsg6x5NyPkaS+zB35ArnB9PCQfaR+tDXOGOAfCT6QflrTCRMZYPlp7uteHFnk+v8AFr89atORDaENzDMNxHrI+deLhgd1HuFPF4ww3UEeR/8AmtxxGwfxJHnl/TWr+YVorz4UdG/ys4+RihMdg1uMTLAx0EaaCddatzWcO48LCegaPgdaExHAs34Lg9oP6/SrhOSM5wiyhPg3BiKyrHe7KXiScy/6j/7a9rf1EYemwHEYhnMsfpFA4x4U+hqehMaNKtEdnfMGKtnCNhVYwoq1cJHhFY4uzbJ0OLdTqaht1MK6jmOK/aBhg/EcTmHhIt/5sttP5f1NScKwXeYO61s5AtoxGgB8QOo21nUUs+03iCpj8RmJCyimNye7UsqxqNMhJ5acyKa8H4wi4O4gTW4EUAjQJIDaDosxXOkrN7fEednLIXDNcLuxYsmZgGEMoI1C/h8zTXDWlsNcbvD40ssAxuNqVj8R00Cnwg6SNtKS2uL2xhu6C+IOGkD8QgjXXcaVBw39o8K3LNxmACytt40HQg5dI0nnWrZCQ6S7LNck5soECdt9tvbQ1zH3AeYE7jePKdKLw1i5vctvbXrl193KmAt4MgzcYn+IxPsAqHND4lexPELZkIlySfxO49vhVRUuH1Amp8ULLN92gQDTQkk+s0RhrQFQ5F8TxMIrAgiQRBHKOYNbtwjSSsDqRRaECt1cH8UnyG3xNTYUIbnD1/Lr5nb2DnQF3hJF0tGYZFA15hmJkbfux7atN2ATFCs/l/X9c6LoCjWeGqUQscuZmOhE6OxmOcGNPOjG4bh3HcXWyPAKXhqDACw/lIOp6nam2IwygADYTHPckmJ9aU8QwecjMAIUAQf4rjDl+6Vmr56dk1tUV/inZq/ZJzLK8mXUH6j20rywZ2+nvNXHHXbgsW7Zbd7nnCqLZjy3PvpGMEIYmDqu45HPp74pVErnIBscVa1cz5iZ0IJBmSNzvpvVqGPGzjb+f6UgVcq3RlGqTOmkan4V5xDi1kTkzTrIywJ1HMiPZWORKTs1x2PcRhLbfhMHy/SlV/BsNhInlofdSo9oCNVTnOrefpU9jtQugdD6iD8OdZ8ZI15EkjNpIOx3Bj61hvkLBhlG3I+8fpR9u5ZvCVYHbbkY5jcULiMAy/hb2HUfqKnT7HYMt5GWGnTY9PaKgdlJ1MNycaz6x86y+pH4k9o1FRLaBGhn4xVLRPZs9sNvCt+9yPrFDvYjQkg+eo/UV62bWf1re1i1jK8+u8enMVoiGCXLBGw+PyqdHIAIJHrI9x2PvohSBpIYfL9KmQQJXVeYOnvHOrTslg4xb8rnx/lWUR9wdTa18ssVlVSJtlNNC4zaizQmJ5eorcxR9BYWrXwoeEVUMK9W3hDeEVhi7NMnQ5SpwKHtmp1NdJgfPHbzD95xfFPdk27boqr1Pdoco8pJJ9a2sY4NO/s01+lSfaJiIx2JJ5XCAPOBVRsXSTvXP5tm66Lqt4J3eIa2GKMckmRMayOY0FH3u3165oZXyVmA92aKrt7EFsOibwSajwOC1k1UgRYU427mWzH1JPzpjh8eI1Wk+HXkBNH27I3Y+ypsY9wWJZkfIkqACxj8OvWiLGJ60nsX2/Ck67gc/XrTHD4eNWNSA1tXZ8hRasIpWtwnQUZbb20WFBLLpt6D9aCujWih0r02QPrSAVXLG5NL7yjM5nmsCdotoD8ZpzfWT5UHi+F2ruZ+6tm7Jk5QSyqzBTr+bKBNVGNpkydNCDH3U+5LMuWb+siJi0I9aDVQ2bKZAya/6xr796b4u0FuWVUAAW7p0AA1e2PpQveFbjkbwg9hzyD1FPX8C3/ILw8C2blxlzZUJy6arBzROh0+lRcR7IJeXvMKQDE5Dtrr/lpktlWW44kfd5SmpjMw1B5iAfP1oXh+Ni3aaSpCr4hy0/lsaXUfce3LTooeNwb2my3FKnz+lDsdNvbXVsXjLF9SmJQTAhwBHt5qdR5acqpnFOBWlnu2MHUE+L2AyARQoXuJfq1qRWFYqZUkEbEGCKZYPtBcWA8OOux9+1LsQoVsupPkI/WvUwV1trcebafP9KHD/kHqLwWvDY+26yseh5dfj0617ewqNqBB6jQ1WsFZKkgsJHukqCIPWKc4K60DoffuawlCno1jK1s8v4V12OYdCPqP0pdfAG4IP9c9qdDFzPyPxFaMikgEf/BpJ12DK89yDFG4e+42Y+3X+dGYjhCGSuh8vPyoRsM6DVcw6jf3GtbTM6aJP2r+AH2/yrKFF9ObR5EGsqxCFjpQWJb50VdbSg7u1bowO44XF1c+CX5UVxqzx1Ru3xq/dnO0FruxL+4E/IGoxRp7LyPR0W1cobi/HrGFUNfuBAZjRjMROig9RSNO01oDTO3osf7iKqnb2/8AtvcqAyKhctMS05YGkxtW05RirMopt7KB2ux4xWNvXLUtba4zKYIkHmQRI9taYHhbbtpVlw/CQohVAFMMLw4TrXG5HShRhsKAIAo/D4EkiTA6nYe6rDZ4eToJY9NTT7hXZlj4riwOQOnwp2xFbwmEw6/ia656IqoP9TT8q9vWMxhLXdr1Zi7H2mPgBVnucOVSYj6fzqFrAGsSamxifD4cINNKIVWNEtazHoKkGmgosCOwkfr1ohKiCRqalsJzoAMQRoN6lsX1B1XMux/UUKzxoPbQ73ZMDYb0WLsLdQGHMSI9tIFvYlNO4UFfzG6IJ/eEKTB8xRfEOIKiNcdsqqp16aGNvOp0dbiAIQSqjKQZDKBsDz6itIK0TLTK7xq5ea9aNtLYc2WLiSVE3NSDodSBypYMJiHusrXEQ5VJKrM/iyjXb82vnTrEXP7QP/IX43bh+lB3g/fZ1a3kKZWBkNIMggjcanfrVOe9+xKho1tcM+7uK9x2zsgMmIy5m0jbWKV27Z7pMsAhTM7HKWH0p5ieIW7aJ3rhMzPlJP7oX2keI7daRW+KIVyKrXPE5UqNILsw8RgbEUpKTVoqDSezLV/UiPVT5Zahx6AYXCEaG5duAnyBc1sti65AIRI/MxLNBM7LAMdJ5VmIRmw/DgAJZ7pAGg2YwJPSnjWnQsj2gazCnxKPXYa/7a8xdjUxp9KMZdTIjlB5bg6cqDuCBI1E/h/Tp8q5nE3T9hdhlGa6p1ByH/kA+lbrZKkZDoPynUa9OYr2yJutpuiH3Fl257VpjLd1bedSB4oLQTlHXY/LlVtNvRKkkjW48AKwgnr7Ig86iuY5bbsS4gTA3n2CkWJxDsfE5b2mPYKFNNQ9xtlowvH7ZGWSCSI0MenlTK1i0eAGU9YO2uxqhkVqCRqDB6jQ0/TRPJnSCqfuj3VlUMcZvj+894U/Eispemw5IButW+EweYyfYKysreTpGMVsvXZzsTeujMlvMB/Eg+ZFWezwZ7JyuuUjlIPyNZWVlXkrl4GdnB0WOGTyn3VlZSk9FLbDsH2bVtblzKOign41YMHwLDpqEL+bH6aD4VlZUx7KmqQ3s2lUQqhfIAD5VJWVldZzgOKwCsZjU0PdwNu2smvayuaUUrNIyfRX8UZJAECo1WKysqDQ9RZ1NbOfyjfmeg8q9rKYmQXjHhHtrW5p4R7ayspDQZw/D23m26hgwgg6jrqDvQz8PRG8MKUOkCPdFZWUeQKz2lW6+KPdBBFq3mmY1ZzpHnNJsPbuOxVrxWOSAD4715WVrObsiEVRYVwFnu0w91S4ILB21YMznWfYPcKUYjhzWSyGIzFlj907enOsrKqXzQd+KJiuM1XmyA3iJDCdCfdrPkahxkG1w1SJGW6Y/wAhI9Na9rKWP6JDn9SCy0jxmdABd/MCdg37w033pVj7ZRoOhmeog17WVK+aLvwP6ZKvIGyDvQf/AAxtof8AvHGh9tPeEMq2wLmqvcKDTnAiQOuutZWVWP6v0Fk6/UV8d7IqZeyYO5U7VSMTZKMVYaj21lZWk4pbJxyb0yA14aysqDQlTCSAQ66/4v8A21lZWVfEiz//2Q==",
 "location": ["Windsor Terrace"],
 "rating": 3.5,
 "about": "A vibrant cafe serving high quality coffee paired with a seasonal menu of brunch and lunch offerings.",
  "mark_as_deleted": False, 
  },
           {
   "id" : 28,
   "name": "Butler Bakeshop",
 "website": "https://www.butler-nyc.com/",
 "logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQprwooO7Rpx72OIsWm-toGFyBX0IJa57iBngfbe3KxECu3SSPD",
 "location": ["Williamsburg"],
 "rating": 4.5,
 "about": "Open for breakfast and lunch, serving fine espresso coffee with sweet and savory goodies courtesy of their Michelin starred pastry chef.",
  "mark_as_deleted": False, 
  },
            {
   "id" : 29,
   "name": "Carthage Must Be Destroyed ",
 "website": "http://www.carthagemustbedestroyed.com/",
 "logo": "http://www.carthagemustbedestroyed.com/images/carthage.png",
 "location": ["Bushwick"],
 "rating": 3.5,
 "about": "Half the fun of enjoying coffee at this secret, pink, Australian organic breakfast and brunch cafe is finding it…",
  "mark_as_deleted": False, 
  },
             {
   "id" : 30,
   "name": "Five Leaves NYC", 
 "website": "https://fiveleavesny.com/",
 "logo": "https://fiveleavesny.com/static/images/frontend/logo.gif ",
 "location": ["Greenpoint"],
 "rating": 4,
 "about": "A place to chill with coffee and brunch for a spot of people and pup watching…there’s even outdoor seating for guests of the 4-legged variety.",
  "mark_as_deleted": False, 
  },
 
]

cafes = [
    "Cafe Grumpy", "Citizens of Chelsea", "Hole in the Wall", "Banter", "Bluestone Lane", "Ruby's Cafe", "Partners Coffee", "Wattle Cafe", "Black Fox Coffee", "Boundless Plains Espresso", "Two Hands NYC", "Five Leaves NYC", "Brunswick Cafe","Abbotsford Road","Butler Bakeshop","Carthage Must Be Destroyed ", "Tulo House", "Charley St", "Happy Bones NYC","Laughing Man Cafe","Supermoon Bakehouse","Coco and Cru","Merriweather NYC","Saltwater NYC","Three Seat Espresso","Bourke St Bakery","Clovelly NYC","St Kilda Coffee", "Little Collins NYC","Hutch and Waldo",
]

locations = [
    "Midtown",
    "West Village",
    "UES",
    "UWS",
    "Financial District",
    "Murray Hill",
    "Chelsea",
    "Greenpoint",
    "Bushwick",
    "Williamsburg",
    "NoLita",
    "Soho",
    "East Village",
    "TriBeCa",
    "LES",
    "Gowanus",
    "Windsor Terrace",
]

@app.route('/')
def home(): 
    return render_template('main.html', data = data, cafes = cafes, locations = locations)

@app.route('/create')
def create(): 
    return render_template('create.html', data = data, cafes = cafes, locations = locations)

@app.route('/search')
def search(): 
    return render_template('search.html', data = data, cafes = cafes, locations = locations)

@app.route('/view/<id>')
def view(id = None): 
    return render_template('view.html', id = id, data = data, cafes = cafes, locations = locations)

@app.route('/save_cafe', methods=['GET','POST'])
def save_cafe():
    global data
    global name 
    global website 
    global logo 
    global location
    global rating 
    global about 
    global id_count
    global cafes 
    global locations

    json_data = request.get_json() 
    name = json_data["name"]
    website =  json_data["website"]
    logo = json_data["logo"]
    location = json_data["location"]
    rating = json_data["rating"]
    about = json_data["about"]
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    new_entry = {
        "id" : id_count,
        "name": name,
        "website":  website,
        "logo": logo, 
        "location": location,
        "rating": rating,
        "about" : about,
        "mark_as_deleted": False, 
    }
    
    data.insert(0,new_entry)
    id_count += 1 

    if name not in cafes: 
        cafes.append(name)

    if location not in locations: 
        locations.append(location)

    return jsonify(data=data, cafes=cafes, locations=locations)

@app.route('/delete_cafe', methods=['GET', 'DELETE'])
def delete_cafe():
    global data

    json_data = request.get_json()   
    ID = json_data["id"]
    ID = int(ID)
    toDel = 0
    for i in range(0,len(data)): 
        if data[i]['id'] == ID:
            data[i]['mark_as_deleted'] = True #set as true 
    
    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)

@app.route('/view/undo_cafe', methods=['GET','POST'])
def undo_delete():
    global data

    json_data = request.get_json()   
    ID = json_data["id"]
    ID = int(ID)
    for i in range(0,len(data)): 
        if data[i]['id'] == ID:
            data[i]['mark_as_deleted'] = False #set as false to undo  
    
    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)

@app.route('/view/update', methods=['GET','POST'])
def update():
    global data
    json_data = request.get_json()   
    ID = json_data["id"]
    LOC = json_data["location"]
    RAT = json_data["rating"]
    WEB = json_data["website"]
    LOG = json_data["logo"]
    ID = int(ID)
    for i in range(0,len(data)): 
        if data[i]['id'] == ID:
          data[i]['website'] = WEB
          data[i]['logo'] = LOG
          data[i]['location'] = LOC
          data[i]['rating'] = RAT 
        
    return jsonify(data = data)


if __name__ == '__main__':
    app.run()