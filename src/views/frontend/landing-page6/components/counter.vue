<template>
  <section class="iq-section-space">
    <div class="container">
      <div class="row">
        <div class="col-md-3 col-sm-6" v-for="(item, index) in list" :key="index">
          <div class="iq-timer style2 mb-5  mb-md-0 mb-lg-0   text-center">
            <div class="iq-icon">  <i aria-hidden="true" :class="item.iconClass"></i> </div>
            <div class="timer-details ">
            <span class="timer dark-timer">
              <span class="counter">{{item.number}}</span>
            </span>
            <span class="timer_postfix dark-timer">M</span><i class="fa fa-percent" aria-hidden="true"></i>
            <p class="dark-timer"> {{ item.title }} </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>

export default {
    name:'Counter',
    components: {
    },
    data () {
    return {
      list: [
        {
          number: 1520,
          iconClass: 'far fa-frown-open',
          title: 'Happy Clients'
        },
        {
          number: 2000,
          iconClass: 'far fa-handshake',
          title: 'Completed Projects'
        },
        {
          number: 150,
          iconClass: 'far fa-user-circle',
          title: 'Team Members'
        },
        {
          number: 750,
          iconClass: 'far fa-check-circle ',
          title: 'Questions Answered'
        }
      ],
      
    }
  }
}
</script>