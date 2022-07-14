<template>
  <errors-layouts>
    <h1 class="error-text font-weight-bold">400</h1>
    <h4 class="mt-4">
      <i class="fa fa-thumbs-down text-danger"></i> Bad Request
    </h4>
    <p>Your Request resulted in an error</p>
  </errors-layouts>
</template>

<script>
import ErrorsLayouts from "../../components/Layouts/ErrorsLayouts.vue";
export default {
  components: { ErrorsLayouts },
};
</script>
