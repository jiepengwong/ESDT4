var template1 = `
                <div>
                    <nav class="navbar navbar-expand-lg navbar-light bg-light">
                        <div class="container-fluid">
                        <a class="navbar-brand">
                            Henesys Grocery MarketPlace
                        </a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                        <div class="row mx-1">

                            <div class="col-2">
                            <ul class="navbar-nav">
                            <li class="nav-item" v-for="link in links">
                                <a class="nav-link" :href="link.link">
                                    {{link.name}}
                                </a>
                            </li>

                            <button v-if="isSignedIn" @click="signOut()" type="button" class="btn btn-success btn-floating mx-1" style="">
                                            SignOut
                            </button>
                            <button v-if="!isSignedIn" @click="googleAuth()" type="button" class="btn btn-success btn-floating mx-1" style="">
                            Login
                            </button>
                        </ul>
                            </div>
                        </div>
                        </nav> {{inSignedIn}}
                    </div>`;
var links1 = [
    {"link":"cataloguenew.php", "name": "Catalogue"},
    {"link":"myoffers.html", "name": "My Offers"},
    {"link":"mylistings.html", "name": "My Listings"},
    {"link": "createlisting.php", "name": "Sell"},
    {'link':"myprofile.html",'name':'My Profile'}
    ];
