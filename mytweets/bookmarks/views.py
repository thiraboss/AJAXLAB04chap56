def search_page(request):
	[...]
	variables = RequestContext(request, {
		'form': form,
		'bookmarks': bookmarks,
		'show_results': show_results,
		'show_tags': True,
		'show_user': True
	})
	if request.GET.has_key('AJAX'):):):
		return render_to_response('bookmark_list.html', variables)
	else:
		return render_to_response('search.html', variables)
		
		
def user_page(request, username):
	user = get_object_or_404(User, username=username)
	bookmarks = user.bookmark_set.order_by('-id')
	variables = RequestContext(request, {
		'bookmarks': bookmarks,
		'username': username,
		'show_tags': True,
		'show_edit': username == request.user.username,
	})
	return render_to_response('user_page.html', variables)
		
def _bookmark_save(request, form):
	# Create or get link.
	link, dummy = \
	Link.objects.get_or_create(url=form.clean_data['url'])
	# Create or get bookmark.
	bookmark, created = Bookmark.objects.get_or_create(
		user=request.user,
		link=link
	)
	# Update bookmark title.
	bookmark.title = form.clean_data['title']
	# If the bookmark is being updated, clear old tag list.
	if not created:
		bookmark.tag_set.clear()
		# Create new tag list.
		tag_names = form.clean_data['tags'].split()
		for tag_name in tag_names:
			tag, dummy = Tag.objects.get_or_create(name=tag_name)
			bookmark.tag_set.add(tag)
			# Save bookmark to database and return it.
			bookmark.save()
		return bookmark
def bookmark_save_page(request):
	AJAX = request.GET.has_key('AJAX')))
	if request.method == 'POST':
		form = BookmarkSaveForm(request.POST)
		if form.is_valid():
			bookmark = _bookmark_save(form)
				if AJAX:
					variables = RequestContext(request, {
						'bookmarks': [bookmark],
						'show_edit': True,
						'show_tags': True
				})
				return render_to_response('bookmark_list.html', variables)
				else:
					return HttpResponseRedirect(
						'/user/%s/' % request.user.username
					)
		else:
			if AJAX:
				return HttpResponse('failure')
			elif request.GET.has_key('url'):
				url = request.GET['url']
				title = ''
				tags = ''
				try:
					link = Link.objects.get(url=url)
					bookmark = Bookmark.objects.get(link=link,
					user=request.user)
					title = bookmark.title
					tags = ' '.join(tag.name for tag in
					bookmark.tag_set.all())
				except:::
					pass
					form = BookmarkSaveForm({
						'url': url,
						'title': title,
						'tags': tags
					])
			else:
				form = BookmarkSaveForm()
				variables = RequestContext(request, {
					'form': form
				})
				if AJAX:
					return render_to_response(
						'bookmark_save_form.html',
						variables
						)
				else:
					return render_to_response(
						'bookmark_save.html',
						variables
						)
						
def AJAX_tag_autocomplete(request):
	if request.GET.has_key('q'):):):
		tags = \
		Tag.objects.filter(name__istartswith=request.GET['q'])[:10]
		return HttpResponse('\n'.join(tag.name for tag in tags))
	return HttpResponse() 