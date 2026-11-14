# Image sources (NASA)

Every picture on the site comes from the **NASA Image and Video Library** (https://images.nasa.gov, API: images-api.nasa.gov). NASA media is generally free to use with credit and no implied NASA endorsement (https://www.nasa.gov/nasa-brand-center/images-and-media/). Some library items belong to partners: always read the credit line of each item.

Each mission has two pictures: a **mission photo** and an **aesthetic photo** (Earthrise, sunsets, crescents, rings). The site picks the best match for the searches below and prints the title, credit and **NASA ID** under every picture in the mission page.

## Lock the exact pictures
Run once on a computer with internet. It saves `data/image_pins.json` (so the site always shows the same pictures, instantly) and rewrites this file with exact NASA IDs and links:

    python3 scripts/pin_nasa_images.py            # pick and pin
    python3 scripts/pin_nasa_images.py --download # also save copies to data/img/

Not happy with a pick? Edit `nasaQueries` (mission photo) or `scenic` (aesthetic photo) for that mission in `data/missions.json`, then run the script again. Or paste a different NASA ID into `data/image_pins.json`.

## Search links (verify and browse alternatives)
| Mission | Mission photo search | Aesthetic photo search |
|---|---|---|
| Apollo 11 Eagle | [Apollo 11 lunar module Eagle](https://images.nasa.gov/search?q=Apollo%2011%20lunar%20module%20Eagle&media=image) | [Apollo 11 Earth rising over lunar horizon](https://images.nasa.gov/search?q=Apollo%2011%20Earth%20rising%20over%20lunar%20horizon&media=image) |
| Lunar Roving Vehicles | [Lunar Roving Vehicle Apollo 15](https://images.nasa.gov/search?q=Lunar%20Roving%20Vehicle%20Apollo%2015&media=image) | [Apollo 15 rover Hadley Delta mountain](https://images.nasa.gov/search?q=Apollo%2015%20rover%20Hadley%20Delta%20mountain&media=image) |
| ALSEP Science Stations | [Apollo 12 ALSEP](https://images.nasa.gov/search?q=Apollo%2012%20ALSEP&media=image) | [Apollo 12 astronaut lunar surface Earth](https://images.nasa.gov/search?q=Apollo%2012%20astronaut%20lunar%20surface%20Earth&media=image) |
| Surveyor 3 | [Surveyor 3 Moon lander](https://images.nasa.gov/search?q=Surveyor%203%20Moon%20lander&media=image) | [Conrad Surveyor 3 Apollo 12 lunar module](https://images.nasa.gov/search?q=Conrad%20Surveyor%203%20Apollo%2012%20lunar%20module&media=image) |
| Sojourner | [Sojourner rover Mars Pathfinder](https://images.nasa.gov/search?q=Sojourner%20rover%20Mars%20Pathfinder&media=image) | [Mars Pathfinder panorama Sojourner](https://images.nasa.gov/search?q=Mars%20Pathfinder%20panorama%20Sojourner&media=image) |
| Spirit | [Spirit rover Gusev crater](https://images.nasa.gov/search?q=Spirit%20rover%20Gusev%20crater&media=image) | [Spirit rover sunset Gusev crater](https://images.nasa.gov/search?q=Spirit%20rover%20sunset%20Gusev%20crater&media=image) |
| Opportunity | [Opportunity rover Meridiani](https://images.nasa.gov/search?q=Opportunity%20rover%20Meridiani&media=image) | [Opportunity Endurance crater panorama](https://images.nasa.gov/search?q=Opportunity%20Endurance%20crater%20panorama&media=image) |
| Viking 1 Lander | [Viking 1 lander Chryse Planitia](https://images.nasa.gov/search?q=Viking%201%20lander%20Chryse%20Planitia&media=image) | [Viking 1 Mars sunset](https://images.nasa.gov/search?q=Viking%201%20Mars%20sunset&media=image) |
| Viking 2 Lander | [Viking 2 lander Utopia Planitia](https://images.nasa.gov/search?q=Viking%202%20lander%20Utopia%20Planitia&media=image) | [Viking 2 Utopia Planitia frost](https://images.nasa.gov/search?q=Viking%202%20Utopia%20Planitia%20frost&media=image) |
| Phoenix | [Phoenix Mars lander](https://images.nasa.gov/search?q=Phoenix%20Mars%20lander&media=image) | [Phoenix lander arctic panorama](https://images.nasa.gov/search?q=Phoenix%20lander%20arctic%20panorama&media=image) |
| InSight | [InSight lander Mars](https://images.nasa.gov/search?q=InSight%20lander%20Mars&media=image) | [InSight lander selfie Mars](https://images.nasa.gov/search?q=InSight%20lander%20selfie%20Mars&media=image) |
| Ingenuity | [Ingenuity Mars helicopter](https://images.nasa.gov/search?q=Ingenuity%20Mars%20helicopter&media=image) | [Ingenuity helicopter shadow Mars](https://images.nasa.gov/search?q=Ingenuity%20helicopter%20shadow%20Mars&media=image) |
| Dawn | [Dawn spacecraft Ceres](https://images.nasa.gov/search?q=Dawn%20spacecraft%20Ceres&media=image) | [Ceres Occator bright spots](https://images.nasa.gov/search?q=Ceres%20Occator%20bright%20spots&media=image) |
| NEAR Shoemaker | [NEAR Shoemaker Eros](https://images.nasa.gov/search?q=NEAR%20Shoemaker%20Eros&media=image) | [Eros asteroid NEAR close up](https://images.nasa.gov/search?q=Eros%20asteroid%20NEAR%20close%20up&media=image) |
| Pioneer 10 | [Pioneer 10 spacecraft](https://images.nasa.gov/search?q=Pioneer%2010%20spacecraft&media=image) | [Jupiter Pioneer 10 image](https://images.nasa.gov/search?q=Jupiter%20Pioneer%2010%20image&media=image) |
| Pioneer 11 | [Pioneer 11 Saturn](https://images.nasa.gov/search?q=Pioneer%2011%20Saturn&media=image) | [Pioneer 11 Saturn rings image](https://images.nasa.gov/search?q=Pioneer%2011%20Saturn%20rings%20image&media=image) |
| Kepler Space Telescope | [Kepler space telescope](https://images.nasa.gov/search?q=Kepler%20space%20telescope&media=image) | [Kepler space telescope stars Cygnus](https://images.nasa.gov/search?q=Kepler%20space%20telescope%20stars%20Cygnus&media=image) |
