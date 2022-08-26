<template>
  <section class="pt-0 prox-fullrside-img">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <VTwoSectionTitle :title-section-prop="titleSectionProp" />
          <div class="row">
            <div class="col-lg-6">
              <div class="text-left">
                <ul class="iq-list wow fadeInUp">
                  <li v-for="(service,index) in service1" :key="index">
                    <i class="fa fa-check" /><span>{{ service.title }} </span>
                  </li>
                </ul>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="text-left">
                <ul class="iq-list wow fadeInUp">
                  <li v-for="(service,index) in service2" :key="index">
                    <i class="fa fa-check" /><span>{{ service.title }} </span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <a class="button gradient-btn button-icon mt-5" href="#"><span class="btn-effect"> Read More</span></a>
        </div>
        <div class="col-lg-6 mt-5 mt-lg-0">
          <div v-for="(list,index) in List" :key="index" :class="index == 1 ? 'color-palette wow fadeInUp text-left ml-lg-5 ml-0'+' '+ list.hoverClass : 'color-palette wow fadeInUp text-left mr-lg-5 mr-0 '+' '+ list.hoverClass">
            <div class="media">
              <div class="circle-icon">
                <i :class="list.icon" aria-hidden="true" />
              </div>
              <div class="media-body">
                <h4 class="color-text mb-2">
                  {{ list.title }}
                </h4>
                <p class="mb-0">
                  {{ list.description }}
                </p>
              </div>
            </div>
          </div>
          <div class="layer_wrap iq-objects  style-one right-top">
            <span class="iq-objects-01">
              <img src="@/assets/images/landing-page/landing-1/400.png" alt="drive02">
            </span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
export default {
  name: 'About',
  data () {
    return {
      titleSectionProp: {
        class: 'text-left  wow fadeInUp  ',
        title: 'Get tips & tricks on how to skyrocket your sales.',
        description: 'Faff about only a quid blower I don’t want no agro bleeding chimney pot burke tosser cras nice one boot fanny.!'
      },

      List: [
        { title: 'Easy to Customize', icon: 'las la-user-cog', hoverClass: 'purple-hover purple-arrow', description: 'There are many variations of passages of Lorem Ipsum available.' },
        { title: 'Multipurpose layout', icon: 'lab la-buffer', hoverClass: 'org-hover org-arrow', description: 'There are many variations of passages of Lorem Ipsum available.' },
        { title: 'Unique Design', icon: 'las la-pencil-ruler', hoverClass: 'green-hover', description: 'There are many variations of passages of Lorem Ipsum available.' }
      ],

      service1: [
        { title: 'Boost SEO ranking' },
        { title: 'Marketing' },
        { title: 'Visual Reviews' }
      ],

      service2: [
        { title: 'Social Sharing' },
        { title: 'Retention' },
        { title: 'Reviews Generation' }
      ]
    }
  }
}
</script>
