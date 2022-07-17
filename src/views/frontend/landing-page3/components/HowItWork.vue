<template>
  <section  class="iq-how-work pt-0">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
           <div class="title-box text-center">
                            <h6 class="title text-white">How Its Work</h6>
                            <h2 class="text-white">How Does Prox</h2>
                        </div>
        </div>
      </div>
      <div class="row">
        <div v-for="(work,index) in works" :key="index" class="col-lg-4">
          <div class="iq-work wow fadeInUp" data-wow-duration="0.5s">
            <BlackCardStyle1>
              <template v-slot:cardNumber>
                {{ work.num }}
              </template>
              <template v-slot:cardContent>
                <i :class="work.icon" />
                <h4 >
                  {{ work.title }}
                </h4>
                <p class="mt-3 mb-0">
                  It is a long established fact that a reader will be distracted by the readable
                  content of a page.
                </p>
              </template>
              <template v-slot:cardLink>
                
               <a class="readmore" href="#"><ion-icon name="arrow-forward"></ion-icon></a>
              
              </template>
            </BlackCardStyle1>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>

import BlackCardStyle1 from "../../../../components/frontend/cards/BlackCardStyle1"
export default {
  name: 'HowItWork',
  components:{
BlackCardStyle1
  },
  data () {
    return {
      works: [
        {
          num: '01',
          icon: 'fas fa-laptop-code mb-3',
          title: 'Easy Install'
        },
        {
          num: '02',
          icon: 'fas fa-file-invoice  mb-3',
          title: ' Create an Account'
        },
        {
          num: '03',
          icon: 'fas fa-cloud-upload-alt  mb-3',
          title: 'Upload Your Data'
        }
      ]
    }
  }
}
</script>
