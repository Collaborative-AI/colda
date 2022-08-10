let musicDuration = 0
export const player = {
  data () {
    return {
      track: {
        name: '',
        artist: '',
        image: '',
        path: ''
      },
      totalDuration: '00:00',
      currentTime: '00:00',
      trackVolume: 100,
      isPlaying: false,
      playButtonClass: 'play',
      audio: new Audio(),
      trackSlider: 0
    }
  },
  mounted () {
    this.isPlaying = false
  },
  methods: {
    loadTrack () {
      this.audio.pause()
      this.resetValues()
      this.audio = new Audio(this.track.path)

      this.audio.addEventListener('timeupdate', () => {
        this.updateTime()
      })
      this.audio.addEventListener('loadeddata', function () {
        musicDuration = this.duration
      })
      setTimeout(() => {
        this.updateTime()
      }, 500)
    },
    resetValues () {
      this.totalDuration = '00:00'
      this.currentDuration = '00:00'
      this.playButtonClass = 'play'
      this.isPlaying = false
    },
    playPauseTrack () {
      if (this.isPlaying) {
        this.audio.pause()
        this.playButtonClass = 'play'
        this.currentDuration = this.audio.currentTime
      } else {
        this.playButtonClass = 'pause'
        this.audio.play()
      }
      this.isPlaying = !this.isPlaying
    },
    seekTo (e) {
      this.audio.currentTime = musicDuration * (e.target.value / 100)
    },
    seekUpdate () {
      //
    },
    updateTime () {
      //

      this.trackSlider = this.audio.currentTime * (100 / musicDuration)
      if (Number.isNaN(this.trackSlider)) {
        this.trackSlider = 0
      }
      let currentMinutes = Math.floor(this.audio.currentTime / 60)
      let currentSeconds = Math.floor(this.audio.currentTime - currentMinutes * 60)
      let durationMinutes = Math.floor(musicDuration / 60)
      let durationSeconds = Math.floor(musicDuration - durationMinutes * 60)
      //
      if (currentSeconds < 10) { currentSeconds = '0' + currentSeconds }
      if (durationSeconds < 10) { durationSeconds = '0' + durationSeconds }
      if (currentMinutes < 10) { currentMinutes = '0' + currentMinutes }
      if (durationMinutes < 10) { durationMinutes = '0' + durationMinutes }
      //
      this.currentTime = currentMinutes + ':' + currentSeconds
      this.totalDuration = durationMinutes + ':' + durationSeconds
    },
    prevTrack (e) {
      this.beforePrevTrackLoad()
      this.loadTrack()
      this.updateTrackArt(e)
      this.afterPrevTrackLoad()
    },
    beforePrevMusicLoad () {
      //
    },
    afterPrevTrackLoad () {
      //
    },
    nextTrack (e) {
      this.beforeNextTrackLoad()
      this.audio.pause()
      this.loadTrack()
      this.updateTrackArt(e)
      this.afterNextTrackLoad()
    },
    beforeNextTrackLoad () {
      //
    },
    afterNextTrackLoad () {
      //
    },
    setVolume (e) {
      this.audio.volume = e.target.value / 100
    },
    updateTrackArt (e) {
      if (e.target.closest('.player') !== null) {
        let trackArt = e.target.closest('.player').querySelector('.track-art')
        if (trackArt !== null && trackArt !== undefined) {
          trackArt.style.backgroundImage = 'url(' + this.track.image + ')'
        }
      }
      if (e.target.closest('.player1') !== null) {
        let trackArt1 = e.target.closest('.player1').querySelector('.track-art')
        if (trackArt1 !== null && trackArt1 !== undefined) {
          trackArt1.style.backgroundImage = 'url(' + this.track.image + ')'
        }
      }
    }
  }
}
