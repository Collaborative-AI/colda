<template>
  <div class="title-box text-left">
    <h6 class="title  text-white md-0  ">
      {{ title }}
    </h6>
    <h2 class="text-white md-3">
      {{ subtitle }}
    </h2>
    <p class="mb-5">
      {{ titlecontent }}
    </p>
  </div>
</template>
<script>
export default {
  name: 'BlackSectionTitle',
  // eslint-disable-next-line vue/require-prop-types
  props: ['title', 'subtitle','titlecontent']
}
</script>
