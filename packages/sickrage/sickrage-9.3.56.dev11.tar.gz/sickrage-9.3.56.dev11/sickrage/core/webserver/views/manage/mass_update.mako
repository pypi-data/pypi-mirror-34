<%inherit file="../layouts/main.mako"/>
<%!
    import sickrage
    from sickrage.core.common import SKIPPED, WANTED, UNAIRED, ARCHIVED, IGNORED, SNATCHED, SNATCHED_PROPER, SNATCHED_BEST, FAILED
    from sickrage.core.common import statusStrings
    from sickrage.core.helpers.compat import cmp
%>
<%block name="content">
    <%namespace file="../includes/quality_defaults.mako" import="renderQualityPill"/>

    <div class="row sickrage-submenu mb-3">
        <div class="col">
            <button class="btn" id="submitMassEdit">${_('Mass Edit')}</button>
            <button class="btn" id="submitMassUpdate">${_('Mass Update')}</button>
            <button class="btn" id="submitMassRescan">${_('Mass Rescan')}</button>
            <button class="btn" id="submitMassRename">${_('Mass Rename')}</button>
            <button class="btn" id="submitMassDelete">${_('Mass Delete')}</button>
            <button class="btn" id="submitMassRemove">${_('Mass Remove')}</button>
            % if sickrage.app.config.use_subtitles:
                <input class="btn" type="button" value="${_('Mass Subtitle')}"
                       id="submitMassSubtitle"/>
            % endif
        </div>
        <div class="col text-right">
            <div class="m-2" id="checkboxControls">
                <label class="badge badge-primary">
                    <input type="checkbox" id="Continuing" checked="checked"/> ${_('Continuing')}
                </label>
                <label class="badge badge-primary">
                    <input type="checkbox" id="Ended" checked="checked"/> ${_('Ended')}
                </label>
            </div>
        </div>
    </div>

    <form name="massUpdateForm" method="post" action="massUpdate">
        <div class="table-responsive">
            <table id="massUpdateTable" class="table" cellspacing="1" border="0" cellpadding="0">
                <thead class="thead-dark">
                <tr>
                    <th class="col-checkbox">
                        <input type="checkbox" class="bulkCheck" id="checkAll"/>
                    </th>
                    <th>${_('Show Name')}</th>
                    <th class="col-quality">${_('Quality')}</th>
                    <th class="col-legend">${_('Sports')}</th>
                    <th class="col-legend">${_('Scene')}</th>
                    <th class="col-legend">${_('Anime')}</th>
                    <th class="col-legend">${_('Season folders')}</th>
                    <th class="col-legend">${_('Skip downloaded')}</th>
                    <th class="col-legend">${_('Paused')}</th>
                    <th class="col-legend">${_('Subtitle')}</th>
                    <th class="col-legend">${_('Default Ep Status')}</th>
                    <th class="col-legend">${_('Status')}</th>
                </tr>
                </thead>

                <tbody>
                    % for curShow in sorted(sickrage.app.showlist, lambda x, y: cmp(x.name, y.name)):
                        <% curEp = curShow.next_aired %>

                        <tr class="${curShow.status}" id="${curShow.indexerid}">
                            <td class="table-fit">
                                <input type="checkbox" class="showCheck"
                                       id="${curShow.indexerid}"
                                       name="${curShow.indexerid}" ${('disabled', '')[bool(not any([sickrage.app.show_queue.isBeingRenamed(curShow), sickrage.app.show_queue.isInRenameQueue(curShow), sickrage.app.show_queue.isInRefreshQueue(curShow), sickrage.app.show_queue.isBeingUpdated(curShow),sickrage.app.show_queue.isInUpdateQueue(curShow), sickrage.app.show_queue.isBeingRefreshed(curShow), sickrage.app.show_queue.isInRefreshQueue(curShow), sickrage.app.show_queue.isBeingRenamed(curShow), sickrage.app.show_queue.isInRenameQueue(curShow), sickrage.app.show_queue.isBeingSubtitled(curShow), sickrage.app.show_queue.isInSubtitleQueue(curShow)]))]}/>
                            </td>
                            <td class="tvShow">
                                <a href="${srWebRoot}/home/displayShow?show=${curShow.indexerid}">${curShow.name}</a>
                            </td>
                            <td class="table-fit">${renderQualityPill(curShow.quality, showTitle=True)}</td>
                            <td class="table-fit">
                                <i class="fa ${("fa-times text-danger", "fa-check text-success")[bool(curShow.is_sports)]}"></i>
                            </td>
                            <td class="table-fit">
                                <i class="fa ${("fa-times text-danger", "fa-check text-success")[bool(curShow.is_scene)]}"></i>
                            </td>
                            <td class="table-fit">
                                <i class="fa ${("fa-times text-danger", "fa-check text-success")[bool(curShow.is_anime)]}"></i>
                            </td>
                            <td class="table-fit">
                                <i class="fa ${("fa-times text-danger", "fa-check text-success")[not bool(curShow.flatten_folders)]}"></i>
                            </td>
                            <td class="table-fit">
                                <i class="fa ${("fa-times text-danger", "fa-check text-success")[bool(curShow.skip_downloaded)]}"></i>
                            </td>
                            <td class="table-fit">
                                <i class="fa ${("fa-times text-danger", "fa-check text-success")[bool(curShow.paused)]}"></i>
                            </td>
                            <td class="table-fit">
                                <i class="fa ${("fa-times text-danger", "fa-check text-success")[bool(curShow.subtitles)]}"></i>
                            </td>
                            <td class="table-fit">${statusStrings[curShow.default_ep_status]}</td>
                            <td class="table-fit">${curShow.status}</td>
                        </tr>
                    % endfor
                </tbody>
            </table>
        </div>
    </form>
</%block>
