<template>
    <aside class="widget-area" id="secondary">
        <div class="widget widget_search">
            <form class="search-form search-top">
                <label>
                    <span class="screen-reader-text">Search for:</span>
                    <input type="search" class="search-field" placeholder="Search...">
                </label>
                <button type="submit">
                    <i class="flaticon-search"></i>
                </button>
            </form>
        </div>
        <div class="widget widget_fria_posts_thumb">
            <h3 class="widget-title">Popular Posts</h3>
            <article class="item">
                <a href="#" class="thumb">
                    <span class="fullimage cover bg1" role="img"></span>
                </a>
                <div class="info">
                    <time class="2022-06-30">June 10, 2022</time>
                    <h4 class="title usmall">
                        <router-link to="/">Making Peace With The Feast Or Famine Of Freelancing</router-link>
                    </h4>
                </div>
            </article>

            <article class="item">
                <a href="#" class="thumb">
                    <span class="fullimage cover bg2" role="img"></span>
                </a>
                <div class="info">
                    <time class="2022-06-30">June 21, 2022</time>
                    <h4 class="title usmall">
                        <router-link to="/">Be healthy, Enjoy life with Trifles organic</router-link>
                    </h4>
                </div>
            </article>

            <article class="item">
                <a href="#" class="thumb">
                    <span class="fullimage cover bg3" role="img"></span>
                </a>
                <div class="info">
                    <time class="2022-06-30">June 30, 2022</time>
                    <h4 class="title usmall">
                        <router-link to="/">Buy organic food online and be healthy</router-link>
                    </h4>
                </div>
            </article>
        </div>

        <div class="widget widget_categories">
            <h3 class="widget-title">Categories</h3>
            <ul>
                <li>
                    <router-link to="/">Business</router-link>
                </li>
                <li>
                    <router-link to="/">Privacy</router-link>
                </li>
                <li>
                    <router-link to="/">Technology</router-link>
                </li>
                <li>
                    <router-link to="/">Tips</router-link>
                </li>
                <li>
                    <router-link to="/">Uncategorized</router-link>
                </li>
            </ul>
        </div>

        <div class="widget widget_recent_comments">
            <h3 class="widget-title">Recent Comments</h3>
            <ul>
                <li>
                    <span class="comment-author-link">
                        <router-link to="/">A WordPress Commenter</router-link>
                    </span>
                    on
                    <router-link to="/">Hello world!</router-link>
                </li>
                <li>
                    <span class="comment-author-link">
                        <router-link to="/">Fria</router-link>
                    </span>
                    on
                    <router-link to="/">Hello world!</router-link>
                </li>
                <li>
                    <span class="comment-author-link">
                        <router-link to="/">Wordpress</router-link>
                    </span>
                    on
                    <router-link to="/">Hello world!</router-link>
                </li>
                <li>
                    <span class="comment-author-link">
                        <router-link to="/">A WordPress Commenter</router-link>
                    </span>
                    on
                    <router-link to="/">Hello world!</router-link>
                </li>
                <li>
                    <span class="comment-author-link">
                        <router-link to="/">Valzo</router-link>
                    </span>
                    on
                    <router-link to="/">Hello world!</router-link>
                </li>
            </ul>
        </div>

        <div class="widget widget_recent_entries">
            <h3 class="widget-title">Recent Posts</h3>
            <ul>
                <li>
                    <router-link to="/">How to Become a Successful Entry Level UX Designer</router-link>
                </li>
                <li>
                    <router-link to="/">How to start your business as an entrepreneur</router-link>
                </li>
                <li>
                    <router-link to="/">How to be a successful entrepreneur</router-link>
                </li>
                <li>
                    <router-link to="/">10 Building Mobile Apps With Ionic And React</router-link>
                </li>
                <li>
                    <router-link to="/">Protect your workplace from cyber attacks</router-link>
                </li>
            </ul>
        </div>

        <div class="widget widget_meta">
            <h3 class="widget-title">Meta</h3>
            <ul>
                <li>
                    <router-link to="/">Log in</router-link>
                </li>
                <li>
                    <router-link to="/">Entries 
                        <abbr title="Really Simple Syndication">RSS</abbr>
                    </router-link>
                </li>
                <li>
                    <router-link to="/">Comments 
                        <abbr title="Really Simple Syndication">RSS</abbr>
                    </router-link>
                </li>
                <li>
                    <router-link to="/">WordPress.org</router-link>
                </li>
            </ul>
        </div>

        <div class="widget widget_archive">
            <h3 class="widget-title">Archives</h3>
            <ul>
                <li>
                    <router-link to="/">May 2022</router-link>
                </li>
                <li>
                    <router-link to="/">April 2022</router-link>
                </li>
                <li>
                    <router-link to="/">June 2022</router-link>
                </li>
            </ul>
        </div>

        <div class="widget widget_tag_cloud">
            <h3 class="widget-title">Tags</h3>
            <div class="tagcloud section-bottom">
                <router-link to="/">
                    IT 
                    <span class="tag-link-count"> (3)</span>
                </router-link>
                <router-link to="/">
                    Valzo 
                    <span class="tag-link-count"> (3)</span>
                </router-link>
                <router-link to="/">
                    Games 
                    <span class="tag-link-count"> (2)</span>
                </router-link>
                <router-link to="/">
                    Fashion 
                    <span class="tag-link-count"> (2)</span>
                </router-link>
                <router-link to="/">
                    Travel 
                    <span class="tag-link-count"> (1)</span>
                </router-link>
                <router-link to="/">
                    Smart 
                    <span class="tag-link-count"> (1)</span>
                </router-link>
                <router-link to="/">
                    Marketing 
                    <span class="tag-link-count"> (1)</span>
                </router-link>
                <router-link to="/">
                    Tips 
                    <span class="tag-link-count"> (2)</span>
                </router-link>
            </div>
        </div>
    </aside>
</template>

<script>
    export default {
        name: 'Sidebar'
    }
</script>