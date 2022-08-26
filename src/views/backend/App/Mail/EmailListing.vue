<template>
  <b-container fluid>
    <b-row>
      <b-col lg="3">
        <card>
          <template v-slot:body>
            <div class="iq-email-list">
              <b-button variant="primary" size="lg" class="font-size-16 p-3 mb-3" block v-b-modal.compose-email-popup><i class="ri-send-plane-line mr-2"></i>New Message</b-button>
              <tab-nav :pills="true" vertical id="myTab" class="iq-email-ui nav flex-column nav-pills" @change="updateTab">
                <tab-nav-items li-class="nav-link active" :active="true" id="mail-inbox-tab" ariaControls="mail-inbox" role="tab" :ariaSelected="true" >
                  <template v-slot:title>
                    <i class="ri-mail-line" />Inbox<span class="badge badge-primary ml-2">4</span>
                  </template>
                </tab-nav-items>
                <tab-nav-items li-class="nav-link" :active="false" id="mail-starred-tab" ariaControls="mail-starred" role="tab" :ariaSelected="true">
                  <template v-slot:title>
                    <i class="ri-star-line" />Starred
                  </template>
                </tab-nav-items>
                <tab-nav-items li-class="nav-link" :active="false" id="mail-snoozed-tab" ariaControls="mail-snoozed" role="tab" :ariaSelected="true">
                  <template v-slot:title>
                    <i class="ri-time-line" />Snoozed
                  </template>
                </tab-nav-items>
                <tab-nav-items li-class="nav-link" :active="false" id="mail-draft-tab" ariaControls="mail-draft" role="tab" :ariaSelected="true">
                  <template v-slot:title>
                    <i class="ri-file-list-2-line" />Draft
                  </template>
                </tab-nav-items>
                <tab-nav-items li-class="nav-link" :active="false" id="mail-sent-tab" ariaControls="mail-sent" role="tab" :ariaSelected="true">
                  <template v-slot:title>
                    <i class="ri-mail-send-line" />Sent Mail
                  </template>
                </tab-nav-items>
                <tab-nav-items li-class="nav-link" :active="false" id="mail-trash-tab" ariaControls="mail-trash" role="tab" :ariaSelected="true">
                  <template v-slot:title>
                    <i class="ri-delete-bin-line" />Trash
                  </template>
                </tab-nav-items>
                <tab-nav-items li-class="nav-link" :active="false" id="mail-important-tab" ariaControls="mail-important" role="tab" :ariaSelected="true">
                  <template v-slot:title>
                    <i class="ri-bookmark-line" />Important
                  </template>
                </tab-nav-items>
                <tab-nav-items li-class="nav-link" :active="false" id="mail-spam-tab" ariaControls="mail-spam" role="tab" :ariaSelected="true">
                  <template v-slot:title>
                    <i class="ri-spam-line" />Spam
                  </template>
                </tab-nav-items>
              </tab-nav>
              <h6 class="mt-4 mb-3">Labels</h6>
              <ul class="iq-email-ui iq-email-label">
                <li><a href="#"><i class="ri-focus-fill text-primary"></i>Personal</a></li>
                <li><a href="#"><i class="ri-focus-fill text-danger"></i>Company</a></li>
                <li><a href="#"><i class="ri-focus-fill text-success"></i>Important</a></li>
                <li><a href="#"><i class="ri-focus-fill text-info"></i>Private</a></li>
                <li><a href="#"><i class="ri-focus-fill text-warning"></i>Private</a></li>
                <li><a href="#"><i class="ri-add-circle-line"></i>Add New Labels</a></li>
              </ul>
              <div class="iq-progress-bar-linear d-inline-block w-100">
                <h6 class="mt-4 mb-3">Storage</h6>
                <div class="iq-progress-bar-linear d-inline-block w-100">
                  <b-progress :value="95" class="iq-progress-bar" variant="danger" ></b-progress>
                </div>
                <span class="mt-1 d-inline-block w-100">13.02 GB (95%) of 15 GB used</span>
              </div>
            </div>
          </template>
        </card>
      </b-col>
      <b-col lg="9">
        <card>
          <div class="iq-email-to-list p-3">
            <div class="d-flex justify-content-between">
              <ul>
                <li>
                  <a href="#">
                    <div class="custom-control custom-checkbox">
                      <input type="checkbox" class="custom-control-input" id="customCheck1">
                      <label class="custom-control-label" for="customCheck1"><i class="ri-arrow-down-s-line"></i></label>
                    </div>
                  </a>
                </li>
                <li v-b-tooltip.top title="Reload"><a href="#"><i class="ri-restart-line"></i></a></li>
                <li v-b-tooltip.top title="Archive"><a href="#"><i class="ri-mail-open-line"></i></a></li>
                <li v-b-tooltip.top title="Spam"><a href="#"><i class="ri-information-line"></i></a></li>
                <li v-b-tooltip.top title="Delete"><a href="#"><i class="ri-delete-bin-line"></i></a></li>
                <li v-b-tooltip.top title="Inbox"><a href="#"><i class="ri-mail-unread-line"></i></a></li>
                <li v-b-tooltip.top title="Zoom"><a href="#"><i class="ri-drag-move-2-line"></i></a></li>
              </ul>
              <div class="iq-email-search d-flex">
                <form class="mr-3 position-relative">
                  <div class="form-group mb-0">
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Search">
                    <a class="search-link" href="#"><i class="ri-search-line" /></a>
                  </div>
                </form>
                <ul>
                  <li class="mr-3">
                    <a class="font-size-14" href="javascript:void(0)">
                      1 - 50 of 505
                    </a>
                  </li>
                  <li v-b-tooltip.top title="Previous"><a href="#"><i class="ri-arrow-left-s-line"></i></a></li>
                  <li v-b-tooltip.top title="Next"><a href="#"><i class="ri-arrow-right-s-line"></i></a></li>
                  <li class="mr-0" v-b-tooltip.top title="Setting"><a href="#"><i class="ri-list-settings-line"></i></a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="iq-email-listbox">
            <tab-content>
              <EmailDetail :active="active" :item="item" @update="closeDetail" />
              <tab-content-item :active="true" id="mail-inbox" aria-labelled-by="mail-inbox-tab" role="tabpanel">
                <ul class="iq-email-sender-list">
                  <li v-for="(items,index) in inboxItems" :key="index" :class="items.is_unread ? 'iq-unread' : ''">
                    <EmailItem :items="items" @update="openDetail"/>
                  </li>
                </ul>
              </tab-content-item>
              <tab-content-item :active="false" id="mail-starred" aria-labelled-by="mail-starred-tab" role="tabpanel">
                <ul class="iq-email-sender-list">
                  <li v-for="(items,index) in starredItems" :key="index" :class="items.is_unread ? 'iq-unread' : ''">
                    <EmailItem :items="items" @update="openDetail"/>
                  </li>
                </ul>
              </tab-content-item>
              <tab-content-item :active="false" id="mail-snoozed" aria-labelled-by="mail-snoozed-tab" role="tabpanel">
                <ul class="iq-email-sender-list">
                  <li v-for="(items,index) in starredItems" :key="index" :class="items.is_unread ? 'iq-unread' : ''">
                    <EmailItem :items="items" @update="openDetail"/>
                  </li>
                </ul>
              </tab-content-item>
              <tab-content-item :active="false" id="mail-draft" aria-labelled-by="mail-draft-tab" role="tabpanel">
                <ul class="iq-email-sender-list">
                  <li v-for="(items,index) in draftItems" :key="index" :class="items.is_unread ? 'iq-unread' : ''">
                    <EmailItem :items="items" @update="openDetail"/>
                  </li>
                </ul>
              </tab-content-item>
              <tab-content-item :active="false" id="mail-sent" aria-labelled-by="mail-sent-tab" role="tabpanel">
                <ul class="iq-email-sender-list">
                  <li v-for="(items,index) in sendItems" :key="index" :class="items.is_unread ? 'iq-unread' : ''">
                    <EmailItem :items="items" @update="openDetail"/>
                  </li>
                </ul>
              </tab-content-item>
              <tab-content-item :active="false" id="mail-trash" aria-labelled-by="mail-trash-tab" role="tabpanel">
                <ul class="iq-email-sender-list">
                  <li v-for="(items,index) in deleteItems" :key="index" :class="items.is_unread ? 'iq-unread' : ''">
                    <EmailItem :items="items" @update="openDetail"/>
                  </li>
                </ul>
              </tab-content-item>
              <tab-content-item :active="false" id="mail-important" aria-labelled-by="mail-important-tab" role="tabpanel">
                <ul class="iq-email-sender-list">
                  <li v-for="(items,index) in starredItems" :key="index" :class="items.is_unread ? 'iq-unread' : ''">
                    <EmailItem :items="items" @update="openDetail"/>
                  </li>
                </ul>
              </tab-content-item>
              <tab-content-item :active="false" id="mail-spam" aria-labelled-by="mail-spam-tab" role="tabpanel">
                <ul class="iq-email-sender-list">
                  <li v-for="(items,index) in spamItems" :key="index" :class="items.is_unread ? 'iq-unread' : ''">
                    <EmailItem :items="items" @update="openDetail"/>
                  </li>
                </ul>
              </tab-content-item>
            </tab-content>
          </div>
        </card>
      </b-col>
      <b-modal v-model="show" id="compose-email-popup" size="lg" hide-footer hide-header content-class="border-0" dialog-class="m-0" static body-class="p-0" class="compose-popup modal-sticky-bottom-right modal-sticky-lg" cancel-title="Close">
        <ComposeBody class="mb-0" :modal="true" @close="closeModal"/>
      </b-modal>
    </b-row>
  </b-container>
</template>
<script>
// import { sofbox } from '../../../config/pluginInit'
import { inboxEmailData, draftEmailsData, sendEmailData, spamEmailsData, starredEmailsData, deletedEmailsData } from '../../../../FackApi/api/email'
import EmailDetail from './EmailDetail'
import EmailItem from './EmailItem'
import ComposeBody from './ComposeBody'
export default {
  name: 'EmailListing',
  components: { ComposeBody, EmailItem, EmailDetail },
  mounted () {
    // sofbox.index()
  },
  data () {
    return {
      show: false,
      inboxItems: inboxEmailData,
      starredItems: starredEmailsData,
      draftItems: draftEmailsData,
      sendItems: sendEmailData,
      spamItems: spamEmailsData,
      deleteItems: deletedEmailsData,
      active: false,
      dataItem: {
        is_selected: false,
        is_unread: false,
        favorite: true,
        title: '',
        subject: '',
        emailTime: ''
      }
    }
  },
  computed: {
    item () {
      return this.dataItem
    }
  },
  methods: {
    openDetail () {
      this.active = true
      // this.dataItem = items
    },
    closeDetail () {
      this.active = false
    },
    updateTab () {
      this.active = false
    },
    closeModal () {
      this.show = false
    }
  }
}
</script>
