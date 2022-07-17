<template>
  <div>
      <h4 class="mb-4">{{ title }}</h4>
      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-6 col-6">
        <ul class="menu list-unstyled p-0 m-0">
          <li v-for="(list,value) in content" :key="value">
            <a :href="list.href">{{ list.title }}</a>
          </li>
        </ul>
        </div>
        <div class="col-lg-6 col-md-6 col-sm-6 col-6 wow fadeInUp" data-wow-delay=".5s" style="visibility: visible; animation-delay: 0.5s; animation-name: F;">
        <ul class="menu list-unstyled p-0 m-0">
          <li v-for="(list,value1) in content1" :key="value1">
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
  props: ['title', 'content', 'content1']
}
</script>
