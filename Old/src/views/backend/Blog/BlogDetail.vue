<template>
   <b-container fluid="">
      <b-row>
         <b-col lg="12">
            <card class="card-block card-stretch card-height blog blog-detail">
                  <template v-slot:body>
                     <div class="image-block">
                        <img src="../../../assets/images/blog/01.jpg" class="img-fluid rounded w-100" alt="blog-img">
                     </div>
                     <div class="blog-description mt-3">
                        <div class="blog-meta d-flex flex-wrap align-items-center mb-3">
                           <div class="date mr-4"><i class="ri-calendar-2-fill pr-2"></i>March 21, 2020</div>
                           <div class="author mr-4"><i class="ri-user-fill pr-2"></i>By: Admin</div>
                           <div class="hit mr-4"><i class="las la-heart pr-2"></i>0 Hits</div>
                           <div class="comments"><i class="ri-chat-3-fill pr-2"></i>82 comments</div>
                        </div>
                        <h5 class="mb-2">There are many variations of passages of Lorem Ipsum available form look even slightly believable.</h5>
                        <p>Voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
                        <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever.</p>
                        <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.</p>
                        <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus.</p> <a href="#" tabindex="-1">Read More <i class="ri-arrow-right-s-line"></i></a>
                     </div>
                  </template>
            </card>
         </b-col>
         <b-col lg="12">
            <card class="card-block card-stretch card-height blog user-comment" headerClass=" d-flex justify-content-between">
               <template v-slot:headerTitle>
                        <h4 class="card-title">User Comment</h4>
               </template>
               <template v-slot:body>
                     <b-row>
                        <b-col lg="6">
                           <card class="card-transparent card-block card-stretch card-height blog" bodyClass="p-0">
                              <template v-slot:body>
                                 <div class="d-flex align-items-center">
                                    <div class="user-image mb-3">
                                       <img class="avatar-80 rounded" src="../../../assets/images/user/01.jpg" alt="#" data-original-title="" title="">
                                    </div>
                                    <div class="ml-3">
                                       <h5>Gurt Mistrioty</h5>
                                       <p>Web Developer</p>
                                    </div>
                                 </div>
                                 <div class="blog-description">
                                    <div class="d-flex align-items-center justify-content-between mb-2"> <a href="#" class="comments"><i class="ri-chat-3-fill pr-2"></i>82 comments</a>
                                       <span class="font-size-12 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star-half-o"></i>
                                          </span>
                                    </div>
                                    <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident.</p>
                                 </div>
                              </template>
                           </card>
                        </b-col>
                        <b-col lg="6">
                           <card class="card-transparent card-block card-stretch card-height blog" bodyClass="p-0">
                              <template v-slot:body>
                                 <div class="d-flex align-items-center">
                                    <div class="user-image mb-3">
                                       <img class="avatar-80 rounded" src="../../../assets/images/user/02.jpg" alt="#" data-original-title="" title="">
                                    </div>
                                    <div class="ml-3">
                                       <h5>Tom Cruise</h5>
                                       <p>Web Designer</p>
                                    </div>
                                 </div>
                                 <div class="blog-description">
                                    <div class="d-flex align-items-center justify-content-between mb-2"> <a href="#" class="comments"><i class="ri-chat-3-fill pr-2"></i>98 comments</a>
                                       <span class="font-size-12 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                          </span>
                                    </div>
                                    <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum Many desktop publishing packages and web page editors now use Lorem Ipsum.</p>
                                 </div>
                              </template>
                           </card>
                        </b-col>
                        <b-col lg="6">
                           <card class="card-transparent card-block card-stretch card-height blog" bodyClass="p-0">
                              <template v-slot:body>
                                 <div class="d-flex align-items-center">
                                    <div class="user-image mb-3">
                                       <img class="avatar-80 rounded" src="../../../assets/images/user/03.jpg" alt="#" data-original-title="" title="">
                                    </div>
                                    <div class="ml-3">
                                       <h5>Walter Hucko</h5>
                                       <p>Web Designer</p>
                                    </div>
                                 </div>
                                 <div class="blog-description">
                                    <div class="d-flex align-items-center justify-content-between mb-2"> <a href="#" class="comments"><i class="ri-chat-3-fill pr-2"></i>28 comments</a>
                                       <span class="font-size-12 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star-half-o"></i>
                                             <i class="fa fa-star-o"></i>
                                          </span>
                                    </div>
                                    <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable.</p>
                                 </div>
                              </template>
                           </card>
                        </b-col>
                        <b-col lg="6">
                           <card class="card-transparent card-block card-stretch card-height blog" bodyClass="p-0">
                              <template v-slot:body>
                                 <div class="d-flex align-items-center">
                                    <div class="user-image mb-3">
                                       <img class="avatar-80 rounded" src="../../../assets/images/user/04.jpg" alt="#" data-original-title="" title="">
                                    </div>
                                    <div class="ml-3">
                                       <h5>Tom Cruise</h5>
                                       <p>Web Manager</p>
                                    </div>
                                 </div>
                                 <div class="blog-description">
                                    <div class="d-flex align-items-center justify-content-between mb-2"> <a href="#" class="comments"><i class="ri-chat-3-fill pr-2"></i>98 comments</a>
                                       <span class="font-size-12 text-warning">
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star"></i>
                                             <i class="fa fa-star-half-o"></i>
                                          </span>
                                    </div>
                                    <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration.randomised words which don't look even slightly believable variations of passages.</p>
                                 </div>
                              </template>
                           </card>
                        </b-col>
                        <b-col lg="12">
                           <card class="card-transparent card-block card-stretch card-height blog" bodyClass="p-0" headerClass=" d-flex justify-content-between pl-0">
                              <template v-slot:headerTitle>
                                    <h4 class="card-title">Your Comment</h4>
                              </template>
                              <template v-slot:body>
                                 <form>
                                    <div class="form-group">
                                       <label for="email1">Email address:</label>
                                       <input type="email" class="form-control" id="email1">
                                    </div>
                                    <div class="form-group">
                                       <label for="pwd">Password:</label>
                                       <input type="password" class="form-control" id="pwd">
                                    </div>
                                    <div class="form-group">
                                       <label for="exampleFormControlTextarea1">Comment</label>
                                       <textarea class="form-control" id="exampleFormControlTextarea1" rows="5"></textarea>
                                    </div>
                                    <div class="checkbox mb-3">
                                       <label>
                                          <input type="checkbox"> Remember me</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Submit</button>
                                    <button type="submit" class="btn iq-bg-danger">Cancel</button>
                                 </form>
                              </template>
                           </card>
                        </b-col>
                     </b-row>
               </template>
            </card>
         </b-col>
      </b-row>
   </b-container>
</template>
<script>
export default {
    name:'BlogDetail'
}
</script>