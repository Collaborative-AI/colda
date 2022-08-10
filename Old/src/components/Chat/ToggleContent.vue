<template>
  <div class="chat-user-detail-popup scroller" ref="removeContent">
    <div class="user-profile" :class="center ? 'text-center' : ''">
      <button type="submit" class="close-popup p-3" @click="dismiss"><i class="ri-close-fill" /></button>
      <div class="user text-center mb-4">
        <a class="avatar m-0">
          <slot name="media" />
        </a>
        <slot name="title" />
      </div>
      <hr>
      <div class="user-detail mt-4 pl-4 pr-4" :class="center ? ' text-center '+bodyClass : bodyClass">
        <slot name="body" />
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ToggleContent',
  props: {
    bodyClass: { type: String, default: '' },
    center: { type: Boolean }
  },
  methods: {
    dismiss () {
      this.$refs.removeContent.classList.remove('show')
    }
  }
}
</script>
