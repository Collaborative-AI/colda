<template>
  <div class="widget">
    <h4 class="footer-title iq-rmt-30">
      {{ addressTitle }}
    </h4>
    <div class="row">
      <div class="col-sm-12">
        <ul class="iq-contact">
          <li v-for="(option,index) in addressContent" :key="index">
            <a href="javascript:void(0)">
              <i v-if="option.icon" :class="option.iconClass" />
              <span>{{ option.text }}</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FooterAddress',
  
  props: ['addressTitle', 'addressContent']
}
</script>
