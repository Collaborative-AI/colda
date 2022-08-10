<template>
  <div class="email-app-details" :class="active ? 'show' : ''">
    <div class="card">
      <div class="card-body p-0">
        <div class="">
          <div class="iq-email-to-list p-3">
            <div class="d-flex justify-content-between">
              <ul>
                <li class="mr-3">
                  <a href="javascript: void(0);" @click="closeDetail(item)">
                    <h4 class="m-0"><i class="ri-arrow-left-line" /></h4>
                  </a>
                </li>
                <li v-b-tooltip.top title="Read"><a href="#"><i class="ri-mail-open-line" /></a></li>
                <li v-b-tooltip.top title="Info"><a href="#"><i class="ri-information-line" /></a></li>
                <li v-b-tooltip.top title="Delete"><a href="#"><i class="ri-delete-bin-line" /></a></li>
                <li v-b-tooltip.top title="Unread"><a href="#"><i class="ri-mail-unread-line" /></a></li>
                <li v-b-tooltip.top title="Forward"><a href="#"><i class="ri-folder-transfer-line" /></a></li>
                <li v-b-tooltip.top title="Bookmark"><a href="#"><i class="ri-bookmark-line" /></a></li>
              </ul>
              <div class="iq-email-search d-flex">
                <ul>
                  <li class="mr-3">
                    <a class="font-size-14" href="#">1 of 505</a>
                  </li>
                  <li v-b-tooltip.top title="Previous"><a href="#"><i class="ri-arrow-left-s-line" /></a></li>
                  <li v-b-tooltip.top title="Next"><a href="#"><i class="ri-arrow-right-s-line" /></a></li>
                </ul>
              </div>
            </div>
          </div>
          <hr class="mt-0">
          <div class="iq-inbox-subject p-3">
            <h5 class="mt-0 mb-3">Your elite author Graphic Optimization reward is ready!</h5>
            <div class="iq-inbox-subject-info">
              <div class="iq-subject-info">
                <img :src="require('../../../../assets/images/user/user-1.jpg')" class="img-fluid rounded avatar-100" alt="#">
                <div class="iq-subject-status align-self-center">
                  <h6 class="mb-0">proX team</h6>
                  <div class="dropdown">
                    <a class="dropdown-toggle" href="#"  id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      to Me
                    </a>
                    <div class="dropdown-menu font-size-12" aria-labelledby="dropdownMenuButton">
                      <table class="iq-inbox-details">
                        <tbody>
                        <tr>
                          <td>from:</td>
                          <td>Medium Daily Digest</td>
                        </tr>
                        <tr>
                          <td>reply-to:</td>
                          <td>noreply@gmail.com</td>
                        </tr>
                        <tr>
                          <td>to:</td>
                          <td>iqonicdesigns@gmail.com</td>
                        </tr>
                        <tr>
                          <td>date:</td>
                          <td>13 Dec 2019, 08:30</td>
                        </tr>
                        <tr>
                          <td>subject:</td>
                          <td>The Golden Rule</td>
                        </tr>
                        <tr>
                          <td>security:</td>
                          <td>Standard encryption</td>
                        </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
                <span class="float-right align-self-center">Jan 15, 2029, 10:20AM</span>
              </div>
              <div class="iq-inbox-body mt-5">
                <p>Hi {{ item.title }},</p>
                <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. </p>
                <p>Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
                <p class="mt-5 mb-0">Regards,<span class="d-inline-block w-100">John Deo</span></p>
              </div>
              <hr>
              <div class="attegement">
                <h6 class="mb-2">ATTACHED FILES:</h6>
                <ul>
                  <li class="icon icon-attegment">
                    <i class="fa fa-file-text-o" aria-hidden="true"></i> <span class="ml-1">mydoc.doc</span>
                  </li>
                  <li class="icon icon-attegment">
                    <i class="fa fa-file-text-o" aria-hidden="true"></i> <span class="ml-1">mydoc.pdf</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EmailDetail',
  props: {
    item: { type: Object,
      default: () => ({
        is_selected: false,
        is_unread: false,
        favorite: true,
        title: '',
        subject: '',
        emailTime: ''
      }) },
    active: { type: Boolean, default: false }
  },
  mounted () {
  },
  methods: {
    closeDetail (item) {
      this.$emit('update', item)
    }
  }
}
</script>
