async function getSystem(baseUrl = 'http://localhost:5000') {
	return get(baseUrl, 'v1/system');
}

async function getBookmarks(baseUrl = 'http://localhost:5000') {
	return get(baseUrl, 'v1/bookmarks');
}

function render(data) {
	body = data.body;
	eth0 = body.network.filter((x) => x.interface === 'eth0')[0];
	renderProgressBar('cpu-stat', body.cpu);
	renderProgressBar('ram-stat', body.memory);
	renderProgressBar('disk-stat', body.disk);
	renderProgressBar('net-stat', eth0);
}

function renderBookmarks(data) {
	groups = groupBy(data.body, 'group');
	Object.keys(groups).forEach((key) => {
		elem = document.createElement('div');
		elem.classList.add('group-container');
		elem.innerHTML = `<div class="group-name">${key}</div>`;
		groups[key].forEach((bookmark) => {
			elem.innerHTML += `<div class="link"><a href="${bookmark.url}">${bookmark.label}</a></div>`;
		});
		document.querySelectorAll('#links-container')[0].appendChild(elem);
	});
}

// --- --- --- 

async function get(baseUrl, path) {
	const response = await fetch(`${baseUrl}/${path}`);
	return await response.json();
}

function groupBy(objArray, property) {
	return objArray.reduce((groups, elem) => {
		(groups[elem[property]] = groups[elem[property]] || []).push(elem);
		return groups;
	}, {});
}

function renderProgressBar(id, data) {
	setPercentage(id, data);
	setSubText(id, data);
}

function setPercentage(id, data) {
	percent = data.percent || data.usage_percent || data.speed;
	document.querySelectorAll(`#${id} .second`)[0].innerHTML = `${percent}%`;
	document.querySelectorAll(`#${id} .circle`)[0].dataset['percent'] = percent;
}

function setSubText(id, data) {
	switch (id) {
		case 'cpu-stat':
			text = `<b>TEMP:</b> ${data?.temp}&#176;`;
			break;
		case 'ram-stat':
		case 'disk-stat':
			text = `<b>Total:</b> ${Math.ceil(data?.total)} GB`;
			break;
		case 'net-stat':
			text = `<b>${data?.unit}<b>`;
			break;
		default:
			text = undefined;
			break;
	}
	if (text !== undefined) {
		document.querySelectorAll(`#${id} .third`)[0].innerHTML = text;
	}
}
