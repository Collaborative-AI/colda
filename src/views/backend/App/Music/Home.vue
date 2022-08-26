<template>
  <b-container fluid="">
    <b-row>
      <b-col lg="12">
        <card className="iq-realease" body-class="iq-realeses-back">
          <template v-slot:headerTitle>
            <h4 class="card-title">{{ 'New Realeases' }}</h4>
          </template>
          <template v-slot:body>
            <b-row>
              <b-col lg="5" class="iq-realese-box ">
                <div class="iq-music-img">
                  <div class="equalizer">
                    <span class="bar bar-1"></span>
                    <span class="bar bar-2"></span>
                    <span class="bar bar-3"></span>
                    <span class="bar bar-4"></span>
                    <span class="bar bar-5"></span>
                  </div>
                </div>
                <div class="player1 row">
                  <div class="details1 music-list col-6 col-sm-6 col-lg-6">
                    <div class="now-playing1"></div>
                    <div class="track-art1"></div>
                    <div>
                      <div class="track-name1">Amy Winehouse</div>
                      <div class="track-artist1">DaBaby Featuring</div>
                    </div>
                  </div>
                  <div class="buttons1 col-6 col-sm-2 col-lg-3">
                    <div class="prev-track1"><i class="fa fa-step-backward fa-2x"></i></div>
                    <div class="playpause-track1" @click="playPauseTrack"><i :class="`fa fa-${playButtonClass}-circle fa-2x`"></i></div>
                    <div class="next-track1"><i class="fa fa-step-forward fa-2x"></i></div>
                  </div>
                </div>
              </b-col>
              <b-col lg="7" class="text-white">
                <Slick :option="realeasesBannerOption" class="list-unstyled iq-song-slide mb-0 realeases-banner">
                  <li v-for="(item,index) in songSlide" :key="index" :class="`row ${item.active !== undefined && item.active ? 'active' : '' }`">
                    <div class="d-flex justify-content-between align-items-center">
                      <div class="media align-items-center col-10 col-md-5">
                        <div class="iq-realese-song ">
                          <router-link to="/music-player">
                            <img :src="item.image"  class="img-border-radius avatar-60 img-fluid" alt="">
                          </router-link>
                        </div>
                        <div class="media-body text-white ml-3">
                          <p class="mb-0 iq-music-title">{{ item.title }}</p>
                          <small>{{ item.name }}</small>
                        </div>
                      </div>
                      <p class="mb-0 col-md-2  iq-m-time">{{ item.time }}</p>
                      <p class="mb-0 col-md-2 iq-m-icon"><i class="lar la-star font-size-20"></i></p>
                      <p class="mb-0 col-2 col-md-2"><i class="las la-play-circle font-size-32"></i></p>
                      <div class="iq-card-header-toolbar iq-music-drop d-flex align-items-center  col-md-1">
                        <b-dropdown :id="`dropdownMenuButton${index}`" right variant="none" data-toggle="dropdown">
                          <template v-slot:button-content>
                            <span class="text-primary"><i class="ri-more-fill"></i></span>
                          </template>
                          <b-dropdown-item><i class="ri-eye-fill mr-2"></i>{{ 'view'}}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-delete-bin-6-fill mr-2"></i>{{ 'delete' }}</b-dropdown-item>
                          <b-dropdown-item><i class="ri-file-download-fill mr-2"></i>{{ 'download' }}</b-dropdown-item>
                        </b-dropdown>
                      </div>
                    </div>
                  </li>
                </Slick>
              </b-col>
            </b-row>
          </template>
        </card>
      </b-col>
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
      <b-col lg="12">
        <div class="card">
          <div class="card-header d-flex justify-content-between">
            <div class="iq-header-title">
              <h4 class="card-title">{{ 'Trending Songs' }}</h4>
            </div>
            <div class="d-flex align-items-center iq-view">
              <b class="mb-0 text-primary"><router-link to="albums">{{ 'view more' }}<i class="las la-angle-right"></i></router-link></b>
            </div>
          </div>
          <div class="card-body">
            <ul class="list-unstyled row iq-box-hover mb-0">
              <li v-for="(item,index) in trendingSong" :key="index"  class="col-xl-2 col-lg-3 col-md-4 iq-music-box">
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
          <div class="card-header d-flex justify-content-between">
            <div class="iq-header-title">
              <h4 class="card-title">{{ 'Popular Hindi Songs' }}</h4>
            </div>
            <div class="d-flex align-items-center iq-view">
              <b class="mb-0 text-primary"><router-link to="/albums">{{ 'View more' }}<i class="las la-angle-right"></i></router-link></b>
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
        <b-row>
          <b-col lg="6" md="12">
            <div class="card card-block card-stretch card-height">
              <div class="card-header d-flex justify-content-between align-items-center">
                <div class="iq-header-title">
                  <h4 class="card-title">{{ 'hot songs' }}</h4>
                </div>
                <div id="hot-song-slick-arrow" class="slick-aerrow-block"></div>
              </div>
              <div class="card-body">
                <Slick :option="hotSongOption">
                  <li  v-for="(item,index) in hotSong" :key="index" class="col-lg-12">
                    <div class="card card-transparent">
                      <div class="card-body p-0">
                        <div class="media align-items-center">
                          <div class="iq-thumb-hotsong">
                            <div class="iq-music-overlay"></div>
                            <router-link to="/music-player">
                              <img :src="item.image" class="img-fluid avatar-60" alt="">
                            </router-link>
                            <div class="overlay-music-icon">
                              <router-link to="/music-player">
                                <i class="las la-play-circle font-size-24"></i>
                              </router-link>
                            </div>
                          </div>
                          <div class="media-body ml-3">
                            <h6 class="mb-0 iq-song-title">{{ item.title }}</h6>
                            <small>{{ item.name }}</small>
                          </div>
                        </div>
                      </div>
                    </div>
                  </li>
                </Slick>
              </div>
            </div>
          </b-col>
          <b-col lg="6" md="12">
            <div class="card card-block card-stretch card-height">
              <div class="card-header d-flex justify-content-between align-items-center">
                <div class="iq-header-title">
                  <h4 class="card-title">{{ 'Hot Video Songs' }}</h4>
                </div>
                <div id="hot-video-slick-arrow" class="slick-aerrow-block"></div>
              </div>
              <div class="card-body">
                <Slick :option="hotVideoSongOption">
                  <li v-for="(item,index) in hotVideoSongs" :key="index" class="col-lg-12">
                    <div class="card mb-lg-0">
                      <div class="card-body p-0">
                        <div class="iq-thumb">
                          <video controls>
                            <source :src="item.video" type="video/mp4" />
                          </video>
                        </div>
                        <div class="feature-list text-center">
                          <h6 class="font-weight-600  mb-0">{{ item.title }}</h6>
                          <p class="mb-0">{{ item.view }}</p>
                        </div>
                      </div>
                    </div>
                  </li>
                </Slick>
              </div>
            </div>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
import { core } from '../../../../config/pluginInit'
import { player } from '../../../../mixins/player-mixin'
 import { musics } from '../../../../JsonData/musics'
export default {
  name: 'Dashboard1',
  mixins: [player],
  components: { },
  mounted () {
    core.index()
    this.track = musics[0]
    this.loadTrack()
  },
  data () {
    return {
      songSlide: [
        {
          title: 'DJ Khaled Featuring',
          name: 'Edyta Gorniak',
          image: require('@/assets/images/music-dashboard/realease-song/01.png'),
          time: '9:52',
          link: ''
        },
        {
          title: 'Megan Thee Stallion',
          name: 'Jessie J',
          image: require('@/assets/images/music-dashboard/realease-song/02.png'),
          time: '5.45',
          link: ''
        },
        {
          title: 'Harry Styles',
          name: 'Loreen ',
          image: require('@/assets/images/music-dashboard/realease-song/03.png'),
          time: '7:52',
          link: '',
          active: true
        },
        {
          title: 'Juice WRLD x',
          name: 'Edith Piaf',
          image: require('@/assets/images/music-dashboard/realease-song/04.png'),
          time: '6:18',
          link: ''
        },
        {
          title: 'Chris Brown & Young Thug',
          name: 'Florence Welch',
          image: require('@/assets/images/music-dashboard/realease-song/05.png'),
          time: '9:00',
          link: ''
        },
        {
          title: 'Jawsh 685 x Jason Derulo',
          name: 'Bonnie Tyler',
          image: require('@/assets/images/music-dashboard/realease-song/06.png'),
          time: '6:52',
          link: ''
        },
        {
          title: 'Jawsh 685 x Jason Derulo',
          name: 'Elena Paparizou',
          image: require('@/assets/images/music-dashboard/realease-song/07.png'),
          time: '7:18',
          link: ''
        },
        {
          title: 'Lady Gaga & Ariana Grande',
          name: 'Leona Lewis',
          image: require('@/assets/images/music-dashboard/realease-song/08.png'),
          time: '8:40',
          link: ''
        },
        {
          title: 'Gabby Barrett',
          name: 'Emeli Sandé',
          image: require('@/assets/images/music-dashboard/realease-song/09.png'),
          time: '9:52',
          link: ''
        }
      ],
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
      realeasesBannerOption: {
        slidesToShow: 5,
        speed: 300,
        arrows: false,
        slidesToScroll: 1,
        vertical: true,
        verticalSwiping: true,
        focusOnSelect: true,
        responsive: [{
          breakpoint: 992,
          settings: {
            arrows: false,
            slidesToShow: 3
          }
        },
        {
          breakpoint: 480,
          settings: {
            arrows: false,
            verticalSwiping: false,
            slidesToShow: 4
          }
        }]
      },
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
      },
      trendingSong: [
        {
          title: 'Life Is Good',
          name: 'Billie Eilish',
          image: require('@/assets/images/music-dashboard/tranding-song/01.png')
        },
        {
          title: 'Death Bed',
          name: 'Normani',
          image: require('@/assets/images/music-dashboard/tranding-song/02.png')
        },
        {
          title: 'Falling',
          name: 'Ava Max',
          image: require('@/assets/images/music-dashboard/tranding-song/03.png')
        },
        {
          title: 'The Bones',
          name: 'Ella Mai',
          image: require('@/assets/images/music-dashboard/tranding-song/04.png')
        },
        {
          title: 'Hard To Forget',
          name: 'Moneybagg Yo',
          image: require('@/assets/images/music-dashboard/tranding-song/05.png')
        },
        {
          title: 'The Box',
          name: 'Doja Cat',
          image: require('@/assets/images/music-dashboard/tranding-song/06.png')
        },
        {
          title: 'Die From A Broken',
          name: 'Lauren Jauregui',
          image: require('@/assets/images/music-dashboard/tranding-song/07.png')
        },
        {
          title: 'Hate The Other',
          name: 'City Girls',
          image: require('@/assets/images/music-dashboard/tranding-song/08.png')
        },
        {
          title: 'The Bigger Picture',
          name: 'Hayley Kiyoko',
          image: require('@/assets/images/music-dashboard/tranding-song/09.png')
        },
        {
          title: 'Life\'s A Mess',
          name: 'Juice WRLD',
          image: require('@/assets/images/music-dashboard/tranding-song/10.png')
        },
        {
          title: 'Conversations',
          name: 'Juice WRLD',
          image: require('@/assets/images/music-dashboard/tranding-song/11.png')
        },
        {
          title: 'Rags2Riches',
          name: 'Jessie Reyez',
          image: require('@/assets/images/music-dashboard/tranding-song/12.png')
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
      hotSong: [
        {
          title: 'Said Sum',
          name: 'Moneybagg Yo',
          image: require('@/assets/images/music-dashboard/hot-songs/01.png')
        },
        {
          title: 'Mood Swings',
          name: 'Rico Nasty',
          image: require('@/assets/images/music-dashboard/hot-songs/02.png')
        },
        {
          title: 'Something Special',
          name: 'Kali Uchis',
          image: require('@/assets/images/music-dashboard/hot-songs/03.png')
        },
        {
          title: 'Tell Me U Luv Me',
          name: 'Juice WRLD',
          image: require('@/assets/images/music-dashboard/hot-songs/04.png')
        },
        {
          title: 'Fighting Demons',
          name: 'Black Eyed Peas',
          image: require('@/assets/images/music-dashboard/hot-songs/05.png')
        },
        {
          title: 'Fighting Demons',
          name: 'Juice WRLD',
          image: require('@/assets/images/music-dashboard/hot-songs/06.png')
        },
        {
          title: 'More Than My Hometown ',
          name: 'Keith Urban',
          image: require('@/assets/images/music-dashboard/hot-songs/07.png')
        },
        {
          title: '3 Headed Goat',
          name: 'Clairo',
          image: require('@/assets/images/music-dashboard/hot-songs/08.png')
        }
      ],
      hotSongOption: {
        slidesToShow: 2,
        speed: 300,
        appendArrows: document.getElementById('hot-song-slick-arrow'),
        slidesToScroll: 1,
        rows: 3,
        focusOnSelect: true,
        responsive: [{
          breakpoint: 992,
          settings: {
            arrows: true,
            slidesToShow: 2
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
      hotVideoSongs: [
        {
          title: 'Chicago Freestyle',
          view: '389382k Views',
          video: require('@/assets/images/music-dashboard/song-video/video-1.mp4')
        },
        {
          title: 'Chicago Freestyle',
          view: '389372k Views',
          video: require('@/assets/images/music-dashboard/song-video/video-2.mp4')
        },
        {
          title: 'Breaking Me',
          view: '89382k Views',
          video: require('@/assets/images/music-dashboard/song-video/video-3.mp4')
        }

      ],
      hotVideoSongOption: {
        slidesToShow: 2,
        speed: 300,
        appendArrows: document.getElementById('hot-video-slick-arrow'),
        slidesToScroll: 1,
        focusOnSelect: true,
        responsive: [{
          breakpoint: 992,
          settings: {
            arrows: true,
            slidesToShow: 2
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
  },
  // methods: {
  //   beforePrevTrackLoad () {
  //     this.track = musics[0]
  //   },
  //   beforeNextTrackLoad () {
  //     this.track = musics[1]
  //   }
  // }
}
</script>

<style>
.iq-card-body{
  flex: unset;
}
</style>
