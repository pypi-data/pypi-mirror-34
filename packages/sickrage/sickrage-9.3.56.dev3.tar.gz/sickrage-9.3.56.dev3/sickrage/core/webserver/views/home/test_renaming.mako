<%inherit file="../layouts/main.mako"/>
<%!
    import re
    import datetime
    import calendar

    import sickrage
    from sickrage.core.common import SKIPPED, WANTED, UNAIRED, ARCHIVED, IGNORED, SNATCHED, SNATCHED_PROPER, SNATCHED_BEST, FAILED
    from sickrage.core.common import Quality, qualityPresets, qualityPresetStrings
    from sickrage.core.helpers import srdatetime
    from sickrage.core.updaters import tz_updater
%>
<%block name="content">
    <input type="hidden" id="showID" value="${show.indexerid}"/>
    <h3>${_('Preview of the proposed name changes')}</h3>
    <blockquote>
        % if int(show.air_by_date) == 1 and sickrage.app.config.naming_custom_abd:
    ${sickrage.app.config.naming_abd_pattern}
        % elif int(show.sports) == 1 and sickrage.app.config.naming_custom_sports:
    ${sickrage.app.config.naming_sports_pattern}
        % else:
    ${sickrage.app.config.naming_pattern}
        % endif
    </blockquote>

    <% curSeason = -1 %>
    <% odd = False%>

    <table id="SelectAllTable" class="table" cellspacing="1" border="0" cellpadding="0">
        <thead>
        <tr class="seasonheader" id="season-all">
            <td colspan="4">
                <h2>${_('All Seasons')}</h2>
            </td>
        </tr>
        <tr class="seasoncols" id="selectall">
            <th class="col-checkbox">
                <input type="checkbox" class="seriesCheck" id="SelectAll"/>
            </th>
            <th align="left" valign="top" class="text-nowrap">${_('Select All')}</th>
            <th width="100%" class="col-name d-none"></th>
        </tr>
        </thead>
    </table>

    <br>

    <input type="submit" value="${_('Rename Selected')}" class="btn btn-success"/>
    <a href="${srWebRoot}/home/displayShow?show=${show.indexerid}" class="btn btn-danger">${_('Cancel Rename')}</a>

    <table id="testRenameTable" class="table" cellspacing="1" border="0" cellpadding="0">

        % for cur_ep_obj in ep_obj_list:
        <%
            curLoc = cur_ep_obj.location[len(cur_ep_obj.show.location)+1:]
            curExt = curLoc.split('.')[-1]
            newLoc = cur_ep_obj.proper_path() + '.' + curExt
        %>
        % if int(cur_ep_obj.season) != curSeason:
            <thead>
            <tr class="seasonheader" id="season-${cur_ep_obj.season}">
                <td colspan="4">
                    <br>
                    <h2>${('Season '+str(cur_ep_obj.season), 'Specials')[int(cur_ep_obj.season) == 0]}</h2>
                </td>
            </tr>
            <tr class="seasoncols" id="season-${cur_ep_obj.season}-cols">
                <th class="col-checkbox">
                    <input type="checkbox" class="seasonCheck" id="${cur_ep_obj.season}"/>
                </th>
                <th class="text-nowrap">${_('Episode')}</th>
                <th class="col-name">${_('Old Location')}</th>
                <th class="col-name">${_('New Location')}</th>
            </tr>
            </thead>
        <% curSeason = int(cur_ep_obj.season) %>
        % endif
            <tbody>
                <%
                    odd = not odd
                    epStr = str(cur_ep_obj.season) + "x" + str(cur_ep_obj.episode)
                    epList = sorted([cur_ep_obj.episode] + [x.episode for x in cur_ep_obj.relatedEps])
                    if len(epList) > 1:
                        epList = [min(epList), max(epList)]
                %>
            <tr class="season-${curSeason} ${('wanted', 'good')[curLoc == newLoc]} seasonstyle">
                <td class="col-checkbox">
                    % if curLoc != newLoc:
                        <input type="checkbox" class="epCheck"
                               id="${"{}x{}".format(cur_ep_obj.season, cur_ep_obj.episode)}"
                               name="${"{}x{}".format(cur_ep_obj.season, cur_ep_obj.episode)}"/>
                    % endif
                </td>
                <td align="center" valign="top" class="text-nowrap">${"-".join(map(str, epList))}</td>
                <td width="50%" class="col-name">${curLoc}</td>
                <td width="50%" class="col-name">${newLoc}</td>
            </tr>
            </tbody>

        % endfor
    </table><br>
    <input type="submit" value="${_('Rename Selected')}" class="btn btn-success"/>
    <a href="${srWebRoot}/home/displayShow?show=${show.indexerid}" class="btn btn-danger">${_('Cancel Rename')}</a>
</%block>
