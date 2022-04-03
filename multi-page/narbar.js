var template1 = `
  <header>
  <a href="cataloguenew.php" class="logo"><h3>Henesys Market</h3></a>
  <nav>
      <ul class="nav__link">

          <li v-for="link in links">
              <a class="hover-underline-animation" :href="link.link">
                  {{link.name}}
              </a>
          </li>
          <!-- <li><a class="hover-underline-animation" href="">My Offers</a></li>
          <li><a class="hover-underline-animation" href="">My Listings</a></li>
          <li><a class="hover-underline-animation" href="">My Profile</a></li> -->
          
          <a class="cta" href=""><button  id="sign" v-if="isSignedIn" @click="signOut()">Logout</button></a>
          <a class="cta" href=""><button  v-if="!isSignedIn" @click="googleAuth()"><b>Login</b></button></a>
      </ul>
  </nav>
  

  </header>`;
var links1 = [
    // {"link":"cataloguenew.php", "name": "Catalogue"},
    {"link":"myoffers.html", "name": "My Offers"},
    {"link":"mylistings.html", "name": "My Listings"},
    {"link": "createlisting.php", "name": "Sell"},
    {'link':"myprofile.html",'name':'My Profile'},

    ];
