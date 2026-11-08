import { getCollection } from 'astro:content';
import rss from '@astrojs/rss';
import { SITE_DESCRIPTION, SITE_TITLE } from '../consts';

export async function GET(context) {
	// Drafts show in `npm run dev` but are left out of the production feed.
	const posts = await getCollection(
		'articles',
		({ data }) => import.meta.env.DEV || !data.draft,
	);
	return rss({
		title: SITE_TITLE,
		description: SITE_DESCRIPTION,
		site: context.site,
		items: posts.map((post) => ({
			...post.data,
			link: `/articles/${post.id}/`,
		})),
	});
}
