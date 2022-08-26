<template>
  <b-container fluid>
    <b-row class="row-eq-height">
      <b-col md="12">
        <b-row>
          <b-col md="12">
            <ComposeBody />
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
import ComposeBody from './ComposeBody'
export default {
  name: 'EmailComposes',
  components: { ComposeBody },
  mounted () {
  }
}
</script>
