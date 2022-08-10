<template>
  <div>
    <div class="widget">
      <h4 class="footer-title">
        {{ title }}
      </h4>
      <div>
        <ul class="menu">
          <li v-for="(list,value) in content" :key="value">
            <a :href="list.href">{{ list.title }}</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'FooterLinks',
  props: {
    title: {
      type: String,
      required: true
    },
    content: {
      type: Array,
      required: true
    }

  }
}
</script>
