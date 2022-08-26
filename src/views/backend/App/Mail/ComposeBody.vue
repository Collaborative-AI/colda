<template>
  <div class="card">
    <div class="card-body">
      <div class="row align-items-center">
        <div class="col-md-12 mb-3">
          <h5 class="text-primary float-left"><i class="ri-pencil-fill"></i> Compose Message</h5>
          <button type="submit" class="float-right close-popup" v-if="modal" @click="close" data-dismiss="modal"><i class="ri-close-fill"></i></button>
        </div>
      </div>
      <form class="email-form">
        <div class="form-group row">
          <label for="inputEmail3" class="col-sm-2 col-form-label">To:</label>
          <div class="col-sm-10">
            <Select2 :options="singleOption" v-model="singleSelect" multiple>
                <option>Select</option>
            </Select2>
          </div>
        </div>
        <div class="form-group row">
          <label for="cc" class="col-sm-2 col-form-label">Cc:</label>
          <div class="col-sm-10">
            <Select2 :options="singleOption1" v-model="singleSelect1" multiple>
              <option>Select</option>
            </Select2>
          </div>
        </div>
        <div class="form-group row">
          <label for="subject" class="col-sm-2 col-form-label">Subject:</label>
          <div class="col-sm-10">
            <input type="text"  id="subject" class="form-control">
          </div>
        </div>
        <div class="form-group row">
          <label for="subject" class="col-sm-2 col-form-label">Your Message:</label>
          <div class="col-md-10">
            <textarea class="textarea form-control" rows="5">Next, use our Get Started docs to setup Tiny!</textarea>
          </div>
        </div>
        <div class="form-group row align-items-center pt-3 m-0">
          <div class="d-flex flex-grow-1 align-items-center">
            <div class="send-btn">
              <button type="submit" class="btn btn-primary">Send</button>
            </div>
            <div class="send-panel ">
              <label class="ml-2 mb-0 iq-bg-primary bg-primary-light rounded" for="file"> <input type="file" id="file" style="display: none"> <a><i class="ri-attachment-line text-primary"></i> </a> </label>
              <label class="ml-2 mb-0 iq-bg-primary bg-primary-light rounded"> <a href="javascript:void(0)"> <i class="ri-map-pin-user-line text-primary"></i></a>  </label>
              <label class="ml-2 mb-0 iq-bg-primary bg-primary-light rounded"> <a href="javascript:void(0)"> <i class="ri-drive-line text-primary"></i></a>  </label>
              <label class="ml-2 mb-0 iq-bg-primary bg-primary-light rounded"> <a href="javascript:void(0)"> <i class="ri-camera-line text-primary"></i></a>  </label>
              <label class="ml-2 mb-0 iq-bg-primary bg-primary-light rounded"> <a href="javascript:void(0)"> <i class="ri-user-smile-line text-primary"></i></a>  </label>
            </div>
          </div>
          <div class="d-flex align-items-center">
            <div class="send-panel float-right">
              <label class="ml-2 mb-0 bg-primary-light iq-bg-primary rounded" ><a href="javascript:void(0)"><i class="ri-settings-2-line text-primary"></i></a></label>
              <label class="ml-2 mb-0 bg-primary-light iq-bg-primary rounded"><a href="javascript:void(0)">  <i class="ri-delete-bin-line text-primary"></i></a>  </label>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ComposeBody',
  props: {
    modal: { type: Boolean, default: false }
  },
  data() {
      return {
         singleSelect: '',
         singleSelect1: '',
         singleOption: [
            { id: 1, text: "Petey Cruiser" },
            { id: 2, text: "Bob Frapples" },
            { id: 3, text: "Barb Ackue" },
            { id: 4, text: "Greta Life" }
         ],
         singleOption1: [
            { id: 1, text: "Brock Lee" },
            { id: 2, text: "Rick O'Shea" },
            { id: 3, text: "Cliff Hanger" },
            { id: 4, text: "Barb Dwyer" }
         ],
      }
    },
    methods: {
    close () {
      this.$emit('close', false)
    }
  }
}
</script>
