<template>
  <errors-layouts>
    <h1 class="error-text font-weight-bold">503</h1>
    <h4 class="mt-4">
      <i class="fa fa-times-circle text-danger"></i> Service Unavailable
    </h4>
    <p>Sorry, we are under maintenance!</p>
  </errors-layouts>
</template>

<script>
import ErrorsLayouts from "../../components/Layouts/ErrorsLayouts.vue";
export default {
  components: { ErrorsLayouts },
};
</script>
