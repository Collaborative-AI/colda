<template>
  <b-container fluid>
    <b-row>
      <b-col lg="7">
        <div class="card card-transparent iq-song-back"  :style= "`background: url(${require('@/assets/images/music-dashboard/realease-song/realease-back.jpg')});background-repeat: no-repeat;`" >
          <div class="card-body">
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
              <div class="details1 col-6 col-sm-6 col-lg-6">
                <div class="now-playing1"></div>
                <div class="track-art1"></div>
                <div>
                  <div class="track-name1">{{ track.name }}</div>
                  <div class="track-artist1">{{ track.artist }}</div>
                </div>
              </div>
              <div class="slider_container1 col-sm-5 col-lg-5">
                <div class="current-time1">{{ currentTime }}</div>
                <input type="range" min="1" max="100" value="0" class="seek_slider1" v-model="trackSlider" @change="seekTo" >
                <div class="total-duration1">{{ totalDuration }}</div>
              </div>
              <div class="buttons1 col-6 col-sm-2 col-lg-3 text-white">
                <div class="prev-track"  @click="prevTrack"><i class="fa fa-step-backward fa-lg"></i></div>
                <div class="playpause-track"  @click="playPauseTrack"><i :class="`fa fa-${playButtonClass}-circle fa-2x`"></i></div>
                <div class="next-track"  @click="nextTrack"><i class="fa fa-step-forward fa-lg"></i></div>
              </div>
              <div class="slider_container1 col-sm-4 col-lg-4">
                <i class="fa fa-volume-down"></i>
                <input type="range" min="1" max="100" value="100" v-model="trackVolume"  class="volume_slider1" @change="setVolume">
                <i class="fa fa-volume-up"></i>
              </div>
            </div>
          </div>
        </div>
      </b-col>
      <b-col lg="5">
        <div class="card card-transparent">
          <div class="card-body p-0">
            <ul class="list-unstyled row mb-0">
              <li v-for="(item,index) of albumSong" :key="index" class="col-lg-6 col-md-6">
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
            </ul>
          </div>
        </div>
      </b-col>
      <b-col lg="12">
        <div class="card">
          <div class="card-header d-flex justify-content-between">
            <div class="iq-header-title">
              <h4 class="card-title">{{ 'top songs' }}</h4>
            </div>
            <div class="d-flex align-items-center iq-view">
              <b class="mb-0 text-primary"><router-link to="/latest">{{ 'view more' }}<i class="las la-angle-right"></i></router-link></b>
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
              <h4 class="card-title">{{ 'popular hindi songs' }}</h4>
            </div>
            <div class="d-flex align-items-center iq-view">
              <b class="mb-0 text-primary"><router-link to="/latest">{{ 'view more' }}<i class="las la-angle-right"></i></router-link></b>
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
    </b-row>
  </b-container>
</template>
<script>
import { core } from '../../../../config/pluginInit'
import { player } from '../../../../mixins/player-mixin'
import { musics } from '../../../../JsonData/musics'

export default {
  name: 'Albums',
  mixins: [player],
  components: { },
  mounted () {
    core.index()
    this.track = musics[0]
    this.loadTrack()
  },
  data () {
    return {
      albumSong: [
        {
          title: 'Girls Like You',
          name: 'Juice WRLD',
          image: require('@/assets/images/music-dashboard/album-song/01.png'),
          link: ''
        },
        {
          title: 'Lucid Dreams',
          name: 'Lady Gaga',
          image: require('@/assets/images/music-dashboard/album-song/02.png'),
          link: ''
        },
        {
          title: 'Better Now',
          name: 'Beyonce',
          image: require('@/assets/images/music-dashboard/album-song/03.png'),
          link: ''
        },
        {
          title: 'No Tears Left To Cry',
          name: 'Ariana Grande',
          image: require('@/assets/images/music-dashboard/album-song/04.png'),
          link: ''
        },
        {
          title: 'I Like Me Better',
          name: 'Lauv',
          image: require('@/assets/images/music-dashboard/album-song/05.png'),
          link: ''
        },
        {
          title: 'Whatever It Takes',
          name: 'George Michael',
          image: require('@/assets/images/music-dashboard/album-song/06.png'),
          link: ''
        },
        {
          title: 'In My Blood',
          name: 'Lil Pump',
          image: require('@/assets/images/music-dashboard/album-song/07.png'),
          link: ''
        },
        {
          title: 'Asylum',
          name: 'Shreya Ghoshal',
          image: require('@/assets/images/music-dashboard/album-song/08.png'),
          link: ''
        },
        {
          title: 'This Is America',
          name: 'Drake',
          image: require('@/assets/images/music-dashboard/album-song/09.png'),
          link: ''
        },
        {
          title: 'What Lovers Do',
          name: 'Dolly Parton',
          image: require('@/assets/images/music-dashboard/album-song/10.png'),
          link: ''
        }
      ],
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
      ]
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
