<template>
  <errors-layouts>
    <h1 class="error-text font-weight-bold">500</h1>
    <h4 class="mt-4">
      <i class="fa fa-times-circle text-danger"></i> Internal Server Error
    </h4>
    <p>You do not have permission to view this resource</p>
  </errors-layouts>
</template>

<script>
import ErrorsLayouts from "../../components/Layouts/ErrorsLayouts.vue";
export default {
  components: { ErrorsLayouts },
};
</script>
