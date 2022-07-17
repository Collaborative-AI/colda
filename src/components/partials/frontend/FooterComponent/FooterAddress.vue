<template>
   <div>
    <h4 class="mb-4">{{ addressTitle }}</h4>
        <ul class="iq-contact list-unstyled p-0 m-0">
          <li v-for="(option,index) in addressContent" :key="index">
            <a href="javascript:void(0)">
              <i v-if="option.icon" :class="option.iconClass"></i>
              <span>{{ option.text }}</span>
            </a>
          </li>
        </ul>
  </div>
</template>

<script>
export default {
  name: 'FooterAddress',
  
  props: ['addressTitle', 'addressContent']
}
</script>
