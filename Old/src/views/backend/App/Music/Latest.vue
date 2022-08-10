<template>
  <b-container fluid>
    <b-row>
      <b-col lg="12">
        <div class="card">
          <div class="card-header d-flex justify-content-between align-items-center">
            <div class="iq-header-title">
              <h4 class="card-title">{{ 'Featured Albums' }}</h4>
            </div>
            <div id="feature-album-slick-arrow" class="slick-aerrow-block"></div>
          </div>
          <div class="card-body">
            <Slick :option="featureAlbumOption">
              <li v-for="(item,index) in featureAlbum" :key="index"  class="col-lg-12 iq-music-box">
                <div class="card mb-0">
                  <div class="card-body p-0">
                    <div class="iq-thumb">
                      <div class="iq-music-overlay"></div>
                      <router-link to="/music-player">
                        <img :src="item.image" class="img-border-radius img-fluid w-100" alt="album">
                      </router-link>
                      <div class="overlay-music-icon">
                        <router-link to="/music-player">
                          <i class="las la-play-circle"></i>
                        </router-link>
                      </div>
                    </div>
                    <div class="feature-list text-center">
                      <h6 class="font-weight-600 mb-0">{{ item.title }}</h6>
                      <p class="mb-0">{{ item.name }}</p>
                    </div>
                  </div>
                </div>
              </li>
            </Slick>
          </div>
        </div>
      </b-col>
      <b-col lg="12">
        <div class="card">
          <div class="card-header d-flex justify-content-between">
            <div class="iq-header-title">
              <h4 class="card-title">{{ 'Top Songs' }}</h4>
            </div>
            <div class="d-flex align-items-center iq-view">
              <b class="mb-0 text-primary"><router-link to="/albums">{{ 'view more' }}<i class="las la-angle-right"></i></router-link></b>
            </div>
          </div>
          <div class="card-body">
            <ul class="list-unstyled row iq-box-hover mb-0">
              <li v-for="(item,index) of topSongs" :key="index" class="col-xl-2 col-lg-3 col-md-4 iq-music-box">
                <div class="card">
                  <div class="card-body p-0">
                    <div class="iq-thumb">
                      <div class="iq-music-overlay"></div>
                      <router-link to="/music-player">
                        <img :src="item.image" class="img-border-radius img-fluid w-100" alt="">
                      </router-link>
                      <div class="overlay-music-icon">
                        <router-link to="/music-player">
                          <i class="las la-play-circle"></i>
                        </router-link>
                      </div>
                    </div>
                    <div class="feature-list text-center">
                      <h6 class="font-weight-600 mb-0">{{ item.title }}</h6>
                      <p class="mb-0">{{ item.name }}</p>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </b-col>
      <b-col lg="12">
        <div class="card">
          <div class="card-header d-flex justify-content-between">
            <div class="iq-header-title">
              <h4 class="card-title">{{ 'Popular Hindi Songs' }}</h4>
            </div>
            <div class="d-flex align-items-center iq-view">
              <b class="mb-0 text-primary"><router-link to="/albums">{{ 'view more' }}<i class="las la-angle-right"></i></router-link></b>
            </div>
          </div>
          <div class="card-body">
            <ul class="list-unstyled row iq-box-hover mb-0">
              <li v-for="(item,index) in popularHindiSong" :key="index"  class="col-xl-2 col-lg-3 col-md-4 iq-music-box">
                <div class="card">
                  <div class="card-body p-0">
                    <div class="iq-thumb">
                      <div class="iq-music-overlay"></div>
                      <router-link to="/music-player">
                        <img :src="item.image" class="img-border-radius img-fluid w-100" alt="">
                      </router-link>
                      <div class="overlay-music-icon">
                        <router-link to="/music-player">
                          <i class="las la-play-circle"></i>
                        </router-link>
                      </div>
                    </div>
                    <div class="feature-list text-center">
                      <h6 class="font-weight-600  mb-0">{{ item.title }}</h6>
                      <p class="mb-0">{{ item.name }}</p>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </b-col>
      <b-col lg="12">
        <div class="card">
          <div class="card-header d-flex justify-content-between align-items-center">
            <div class="iq-header-title">
              <h4 class="card-title">{{ 'Featured Albums' }}</h4>
            </div>
            <div id="feature-album-artist-slick-arrow" class="slick-aerrow-block"></div>
          </div>
          <div class="card-body">
            <Slick :option="featureAlbumArtistOption">
              <li v-for="(item,index) in featureAlbumArtist" :key="index"  class="col-lg-12 iq-music-box">
                <div class="iq-thumb-artist">
                  <div class="iq-music-overlay"></div>
                  <router-link to="/music-player">
                    <img :src="item.image" class="img-border-radius img-fluid w-100" alt="album">
                  </router-link>
                  <div class="overlay-music-icon">
                    <router-link to="/music-player">
                      <i class="las la-play-circle"></i>
                    </router-link>
                  </div>
                </div>
                <div class="feature-list text-center">
                  <h6 class="font-weight-600 mb-0">{{ item.title }}</h6>
                </div>
              </li>
            </Slick>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
import { core } from '../../../../config/pluginInit'
export default {
  name: 'Latest',
  components: { },
  mounted () {
    core.index()
  },
  data () {
    return {
      featureAlbum: [
        {
          title: 'Doja Cat',
          name: 'Annie Lennox',
          image: require('@/assets/images/music-dashboard/feature-album/01.png'),
          link: ''
        },
        {
          title: 'Justin Bieber',
          name: 'Sade Adu',
          image: require('@/assets/images/music-dashboard/feature-album/02.png'),
          link: ''
        },
        {
          title: 'Pop Smoke',
          name: 'Cascada',
          image: require('@/assets/images/music-dashboard/feature-album/03.png'),
          link: ''
        },
        {
          title: 'Miranda Lambert',
          name: 'Natasha',
          image: require('@/assets/images/music-dashboard/feature-album/04.png'),
          link: ''
        },
        {
          title: 'Future Featuring',
          name: 'Sophie Ellis',
          image: require('@/assets/images/music-dashboard/feature-album/05.png'),
          link: ''
        },
        {
          title: 'Powfu Featuring',
          name: 'Cheryl Cole',
          image: require('@/assets/images/music-dashboard/feature-album/06.png'),
          link: ''
        },
        {
          title: 'Pop Smoke',
          name: 'Patricia Kaas',
          image: require('@/assets/images/music-dashboard/feature-album/07.png'),
          link: ''
        },
        {
          title: 'Asylum',
          name: 'Shreya Ghoshal',
          image: require('@/assets/images/music-dashboard/feature-album/08.png'),
          link: ''
        },
        {
          title: 'Before You Go',
          name: 'Lewis Capaldi',
          image: require('@/assets/images/music-dashboard/feature-album/09.png'),
          link: ''
        },
        {
          title: 'Don\'t Start Now',
          name: 'Dua Lipa',
          image: require('@/assets/images/music-dashboard/feature-album/08.png'),
          link: ''
        }
      ],
      featureAlbumOption: {
        slidesToShow: 6,
        speed: 300,
        slidesToScroll: 1,
        focusOnSelect: true,
        appendArrows: document.getElementById('feature-album-slick-arrow'),
        responsive: [{
          breakpoint: 1200,
          settings: {
            slidesToShow: 4
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 3
          }
        },
        {
          breakpoint: 480,
          settings: {
            arrows: false,
            autoplay: true,
            slidesToShow: 1
          }
        }]
      },
      topSongs: [
        {
          title: 'Enjoy Yourself',
          name: 'cupcakKe ',
          image: require('@/assets/images/music-dashboard/top-song/01.png')
        },
        {
          title: 'Pretty Heart',
          name: 'Niki',
          image: require('@/assets/images/music-dashboard/top-song/02.png')
        },
        {
          title: 'The Climb Back',
          name: 'King Princess',
          image: require('@/assets/images/music-dashboard/top-song/03.png')
        },
        {
          title: 'Got It On Me',
          name: 'Bulow',
          image: require('@/assets/images/music-dashboard/top-song/04.png')
        },
        {
          title: 'Stuck With U',
          name: 'Tierra Whack',
          image: require('@/assets/images/music-dashboard/top-song/05.png')
        },
        {
          title: 'Be Like That',
          name: 'Ravyn Lenae',
          image: require('@/assets/images/music-dashboard/top-song/06.png')
        },
        {
          title: 'God Whispered ',
          name: 'Amber Mark',
          image: require('@/assets/images/music-dashboard/top-song/07.png')
        },
        {
          title: 'One Of Them Girls',
          name: 'Rina',
          image: require('@/assets/images/music-dashboard/top-song/08.png')
        },
        {
          title: 'Mood Swings',
          name: 'Yaeji',
          image: require('@/assets/images/music-dashboard/top-song/09.png')
        },
        {
          title: 'Something Special',
          name: 'Morgan',
          image: require('@/assets/images/music-dashboard/top-song/10.png')
        },
        {
          title: 'Tell Me U Luv',
          name: 'BbyMutha',
          image: require('@/assets/images/music-dashboard/top-song/11.png')
        },
        {
          title: 'Up Up And Away',
          name: 'Britney',
          image: require('@/assets/images/music-dashboard/top-song/12.png')
        },
        {
          title: 'Fighting Demons',
          name: 'Kylie',
          image: require('@/assets/images/music-dashboard/top-song/13.png')
        },
        {
          title: 'More Than My Ho',
          name: 'Fiona Apple',
          image: require('@/assets/images/music-dashboard/top-song/14.png')
        },
        {
          title: 'Girl Of My Dreams',
          name: 'Frank',
          image: require('@/assets/images/music-dashboard/top-song/15.png')
        },
        {
          title: ' In My Feelings',
          name: 'Drake',
          image: require('@/assets/images/music-dashboard/top-song/16.png')
        },
        {
          title: 'Does To Me',
          name: 'Elvis Presley',
          image: require('@/assets/images/music-dashboard/top-song/17.png')
        },
        {
          title: 'Man Of The Year',
          name: 'Juice WRLD',
          image: require('@/assets/images/music-dashboard/top-song/18.png')
        },
        {
          title: 'Dollaz On',
          name: 'Celine Dion',
          image: require('@/assets/images/music-dashboard/top-song/19.png')
        },
        {
          title: 'Enjoy Yourself',
          name: 'Prince',
          image: require('@/assets/images/music-dashboard/top-song/20.png')
        },
        {
          title: 'The Climb Back',
          name: 'Elton John',
          image: require('@/assets/images/music-dashboard/top-song/21.png')
        },
        {
          title: 'More Than My ',
          name: 'Morgan Wallen',
          image: require('@/assets/images/music-dashboard/top-song/22.png')
        },
        {
          title: 'Girl Of My Dreams',
          name: 'Rod Wave',
          image: require('@/assets/images/music-dashboard/top-song/23.png')
        },
        {
          title: '3 Headed Goat',
          name: 'Mariah Carey',
          image: require('@/assets/images/music-dashboard/top-song/24.png')
        },
        {
          title: 'Something..',
          name: 'Pop Smoke',
          image: require('@/assets/images/music-dashboard/top-song/25.png')
        },
        {
          title: 'I Love My Country',
          name: 'Florida Georgia',
          image: require('@/assets/images/music-dashboard/top-song/26.png')
        },
        {
          title: 'Girls Like You',
          name: 'DaBaby',
          image: require('@/assets/images/music-dashboard/top-song/27.png')
        },
        {
          title: 'I Like It',
          name: 'Post Malone',
          image: require('@/assets/images/music-dashboard/top-song/28.png')
        },
        {
          title: 'Meant To Be',
          name: 'Luke Combs',
          image: require('@/assets/images/music-dashboard/top-song/29.png')
        },
        {
          title: 'God\'s Plan',
          name: 'Drake',
          image: require('@/assets/images/music-dashboard/top-song/30.png')
        }
      ],
      popularHindiSong: [
        {
          title: 'Said Sum',
          name: 'Moneybagg Yo',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/01.png')
        },
        {
          title: 'Toosie Slide',
          name: 'Drake',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/02.png')
        },
        {
          title: 'Girls In The Hood',
          name: 'Megan Thee',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/03.png')
        },
        {
          title: 'Supalonely',
          name: 'BENEE Featuring',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/04.png')
        },
        {
          title: 'Walk Em Down',
          name: 'NLE Choppa',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/05.png')
        },
        {
          title: 'Blood On',
          name: 'Juice WRLD',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/06.png')
        },
        {
          title: 'One Big Country',
          name: 'LOCASH',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/07.png')
        },
        {
          title: 'Righteous',
          name: 'Juice WRLD',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/08.png')
        },
        {
          title: 'Got What I Got',
          name: 'Jason Aldean',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/09.png')
        },
        {
          title: 'I Love My Country',
          name: 'Florida Georgia',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/10.png')
        },
        {
          title: 'Got It On Me',
          name: 'Summer Walker',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/11.png')
        },
        {
          title: 'Like That',
          name: 'Stefflon Don',
          image: require('@/assets/images/music-dashboard/popular-hindi-song/12.png')
        }
      ],
      featureAlbumArtist: [
        {
          title: 'Pixie Lott',
          image: require('@/assets/images/music-dashboard/feature-album-artist/01.png'),
          link: ''
        },
        {
          title: 'Jessie Ware',
          image: require('@/assets/images/music-dashboard/feature-album-artist/02.png'),
          link: ''
        },
        {
          title: 'Alesha Dixon',
          image: require('@/assets/images/music-dashboard/feature-album-artist/03.png'),
          link: ''
        },
        {
          title: 'Sarah Connor',
          image: require('@/assets/images/music-dashboard/feature-album-artist/04.png'),
          link: ''
        },
        {
          title: 'Agnes',
          image: require('@/assets/images/music-dashboard/feature-album-artist/05.png'),
          link: ''
        },
        {
          title: 'Rebecca',
          image: require('@/assets/images/music-dashboard/feature-album-artist/06.png'),
          link: ''
        },
        {
          title: 'Grace',
          image: require('@/assets/images/music-dashboard/feature-album-artist/07.png'),
          link: ''
        },
        {
          title: 'Courtney',
          image: require('@/assets/images/music-dashboard/feature-album-artist/08.png'),
          link: ''
        },
        {
          title: 'Billie Eilish',
          image: require('@/assets/images/music-dashboard/feature-album-artist/09.png'),
          link: ''
        },
        {
          title: 'Normani',
          image: require('@/assets/images/music-dashboard/feature-album-artist/10.png'),
          link: ''
        }
      ],
      featureAlbumArtistOption: {
        slidesToShow: 6,
        speed: 300,
        slidesToScroll: 1,
        appendArrows: document.getElementById('feature-album-artist-slick-arrow'),
        focusOnSelect: true,
        responsive: [{
          breakpoint: 1200,
          settings: {
            slidesToShow: 4
          }
        },
        {
          breakpoint: 992,
          settings: {
            arrows: true,
            slidesToShow: 3
          }
        },
        {
          breakpoint: 480,
          settings: {
            arrows: false,
            autoplay: true,
            slidesToShow: 1
          }
        }]
      }
    }
  }
}
</script>
