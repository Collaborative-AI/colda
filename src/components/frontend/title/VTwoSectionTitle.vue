<template>
  <div :class="'title-box' +' '+ titleSectionProp.class">
    <h2 v-if="titleSectionProp.title" :class="titleSectionProp.titleClass">
      {{ titleSectionProp.title }}
    </h2>
    <p v-if="titleSectionProp.description" :class=" titleSectionProp.descClass">
      {{ titleSectionProp.description }}
    </p>
    <slot name="button" />
  </div>
</template>
<script>
export default {
  name: 'VTwoSectionTitle',
  props: {
    // eslint-disable-next-line vue/require-default-prop
    titleSectionProp: {
      type: Object
    }
  }
}
</script>
