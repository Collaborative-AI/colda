<template>
  <section class="iq-section-space iq-bg-over">
    <div class="container">
      <div class="row">
        <div class="col-md-4">
          <div class="custom-tab">
            
            <tab-nav :pills="true " :vertical="true"  id="Pills-tab" extraclass="text-center mb-5 mb-md-0" role="tablist" aria="vertical">
              <tab-nav-items :active="true" id="development" ariaControls="software-development" role="tab" :ariaSelected="true" title="Software Development" liClass=" nav-item w-inherit"  widthclass="w-100">
                <template v-slot:title>
                  <h5 class="tab-title">Software Development</h5>
                </template>
              </tab-nav-items>
              <tab-nav-items :active="false" id="services"  ariaControls="application-services" role="tab" dataToggle="pill" :ariaSelected="false" title="Application Services" liClass=" nav-item w-inherit"  widthclass="w-100" >
              <template v-slot:title>
                  <h5 class="tab-title">Application Services</h5>
                </template>
                </tab-nav-items>
              <tab-nav-items :active="false" id="analytics" ariaControls="data-analytics" role="tab" :ariaSelected="false" title="Data Analytics" liClass=" nav-item w-inherit"  widthclass="w-100">
            <template v-slot:title>
                  <h5 class="tab-title">Data Analytics</h5>
                </template>
                </tab-nav-items>
                   <tab-nav-items :active="false" id="help-desk-services" ariaControls="tab-help-desk-services" role="tab" :ariaSelected="false" title="Data Analytics" liClass=" nav-item w-inherit"  widthclass="w-100">
            <template v-slot:title>
                  <h5 class="tab-title">Help Desk Services</h5>
                </template>
                </tab-nav-items>
             </tab-nav>
          </div>
        </div>
        <div class="col-md-8">
           <tab-content id="myTabContent">
        
              <tab-content-item :active="true" id="software-development" aria-labelled-by="development">
         
              <h3 class="pb-3">Choose Your Software Development Service</h3>
              <p>Tame your big data through robust solutions that empower data collection, storage,processing and analysis.</p>
              <ul class="iq-list column-2">
                <li><i class="fas fa-check-circle"></i>Advance Advisory Team</li>
                <li><i class="fas fa-check-circle"></i>Professional Consulting Services</li>
                <li><i class="fas fa-check-circle"></i>24/7 Support Help Center</li>
                <li><i class="fas fa-check-circle"></i>Customer Service &amp; Operations</li>
                <li><i class="fas fa-check-circle"></i>There are many variations of passages.</li>
              </ul>
          
              </tab-content-item>
                <tab-content-item :active="false" id="application-services" aria-labelled-by="services">
            
              <h3 class="pb-3">Choose Your Application Service</h3>
              <p>Tame your big data through robust solutions that empower data collection, storage,processing and analysis.</p>
              <ul class="iq-list column-2">
                <li><i class="fas fa-check-circle"></i>Advance Advisory Team</li>
                <li><i class="fas fa-check-circle"></i>Professional Consulting Services</li>
                <li><i class="fas fa-check-circle"></i>24/7 Support Help Center</li>
                <li><i class="fas fa-check-circle"></i>Customer Service &amp; Operations</li>
                <li><i class="fas fa-check-circle"></i>There are many variations of passages.</li>
              </ul>
          
                </tab-content-item>
                   <tab-content-item :active="false" id="data-analytics" aria-labelled-by="analytics">
           
              <h3 class="pb-3">Choose Your Data Analytics Service</h3>
              <p>Tame your big data through robust solutions that empower data collection, storage,processing and analysis.</p>
              <ul class="iq-list column-2">
                <li><i class="fas fa-check-circle"></i>Advance Advisory Team</li>
                <li><i class="fas fa-check-circle"></i>Professional Consulting Services</li>
                <li><i class="fas fa-check-circle"></i>24/7 Support Help Center</li>
                <li><i class="fas fa-check-circle"></i>Customer Service &amp; Operations</li>
                <li><i class="fas fa-check-circle"></i>There are many variations of passages.</li>
              </ul>
         
                   </tab-content-item>
                    <tab-content-item :active="false" id="tab-help-desk-services" aria-labelled-by="help-desk-services">
           
              <h3 class="pb-3">Choose Your Help Desk Service</h3>
              <p>Tame your big data through robust solutions that empower data collection, storage,processing and analysis.</p>
              <ul class="iq-list column-2">
                <li><i class="fas fa-check-circle"></i>Advance Advisory Team</li>
                <li><i class="fas fa-check-circle"></i>Professional Consulting Services</li>
                <li><i class="fas fa-check-circle"></i>24/7 Support Help Center</li>
                <li><i class="fas fa-check-circle"></i>Customer Service &amp; Operations</li>
                <li><i class="fas fa-check-circle"></i>There are many variations of passages.</li>
              </ul>
          
                    </tab-content-item>
      
           </tab-content>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import tabContentItem from '../../../../components/tab/tab-content-item.vue'
export default {
  components: { tabContentItem },
    name: 'Services'
}
</script>