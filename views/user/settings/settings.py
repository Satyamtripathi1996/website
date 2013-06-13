##
#    Copyright (C) 2013 Jessica Tallon & Matt Molyneaux
#   
#    This file is part of Inboxen.
#
#    Inboxen is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Inboxen is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Inboxen.  If not, see <http://www.gnu.org/licenses/>.
##

from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from website.helper.user import user_profile

@login_required
def settings(request):
    error = ""
    
    # check their html preferences
    profile = user_profile(request.user)
    
    # they submitting it?
    if request.method == "POST":
        
        profile.html_preference = int(request.POST["html-preference"])
        profile.save()        
        
        if not error:
            # now redirect back to their profile
            return HttpResponseRedirect("/user/settings")


    context = {
        "page":_("Settings"),
        "error":error,
        "htmlpreference":int(profile.html_preference),
    }

    return render(request, "user/settings.html", context)
