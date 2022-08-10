<template>
  <div class="d-flex align-self-center" @click="openDetail(items)">
    <div class="iq-email-sender-info">
      <div class="iq-checkbox-mail">
        <div class="custom-control custom-checkbox">
          <input type="checkbox" class="custom-control-input" :id="'index-'+items.title">
          <label class="custom-control-label" :for="'index-'+items.title" />
        </div>
      </div>
      <span class="ri-star-line iq-star-toggle" :class="items.favorite ? 'text-warning' : ''" />
      <a href="javascript: void(0);" class="iq-email-title">{{ items.title }}</a>
    </div>
    <div class="iq-email-content">
      <a href="javascript: void(0);" class="iq-email-subject">{{ items.subject }} &nbsp;–&nbsp;
        <span>@Mackenzieniko - Very cool :) Nicklas, You have a new direct message.</span>
      </a>
      <div class="iq-email-date">{{ items.emailTime }}</div>
    </div>
    <ul class="iq-social-media">
      <li><a href="#"><i class="ri-delete-bin-2-line" /></a></li>
      <li><a href="#"><i class="ri-mail-line" /></a></li>
      <li><a href="#"><i class="ri-file-list-2-line" /></a></li>
      <li><a href="#"><i class="ri-time-line" /></a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'EmailItem',
  props: ['items'],
  methods: {
    openDetail (items) {
      this.$emit('update', items)
    }
  }
}
</script>
