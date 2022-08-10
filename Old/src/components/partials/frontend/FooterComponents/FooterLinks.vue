<template>
  <div>
    <h4 class="footer-title">{{ title }}</h4>
    <div class="menu-footer-menu-container">
      <ul class="menu">
        <li v-for="(list,value) in content" :key="value" class="menu-item">
          <!-- <a :href="list.href">{{ list.title }}</a> -->
          <!-- <a v-if="list.title=='Documentation'" target="_blank" :href="list.href">{{list.title}}</a>
          <a v-else-if="list.title=='Tutorials'" target="_blank" :href="list.href">{{list.title}}</a> -->
          <router-link :to="list.href">{{list.title}}</router-link>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
export default {
  name: 'FooterLinks',
  props: ['title', 'content']
}
</script>
