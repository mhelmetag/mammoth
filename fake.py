from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()

@app.route('/', methods=['GET'])
async def root(request):
  data = {
    'data': "\r\n\r\n<div class=\"row mountain-info\">\r\n    <div class=\"form-inline col-sm-12 col-md-12\">\r\n        <span class=\"sort-label\">Sort by</span>\r\n        <label for=\"lift-sort-list\" class=\"ada\" style=\"display: none;\">ctl00$subpage_content_$ctl03</label>\r\n        <select name=\"lift-sort-list\" id=\"lift-sort-list\" class=\"trail-sort form-control\">\r\n            <option  value=\"Name\">Name</option>\r\n            <option Selected value=\"Status\">Status</option>\r\n\r\n        </select>\r\n    </div>\r\n    <div class=\"col-md-12 col-sm-12\">\r\n        <table>\r\n            <tbody>\r\n                <tr>\r\n                    <td class=\"lift-column-heading\" colspan=\"1\"><span>Status</span></td>\r\n                    <td class=\"lift-column-heading\" colspan=\"1\"><span>Name</span></td>\r\n                    <td class=\"lift-column-heading\" colspan=\"1\"><span>Type</span></td>\r\n                    <td class=\"lift-column-heading\" colspan=\"1\"><span>Updated</span></td>\r\n                </tr>\r\n\r\n\r\n\r\n                            <tr class=\"lift-header\">\r\n                                <td class=\"header-description\" colspan=\"4\"><span>Main Lodge</span></td>\r\n                            </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Broadway Express 1</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 12</span></td>\r\n                        <td class=\"lift-chair-icon chair2\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 13</span></td>\r\n                        <td class=\"lift-chair-icon chair2\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon open\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 14</span></td>\r\n                        <td class=\"lift-chair-icon chair2\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>4:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 23</span></td>\r\n                        <td class=\"lift-chair-icon chair3\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Discovery Express 11</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Face Lift Express 3</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Gold Rush Express 10</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Panorama Lower</span></td>\r\n                        <td class=\"lift-chair-icon gondola\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Panorama Upper</span></td>\r\n                        <td class=\"lift-chair-icon gondola\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Stump Alley Express 2</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Unbound Express 6</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                            <tr class=\"lift-header\">\r\n                                <td class=\"header-description\" colspan=\"4\"><span>Canyon Lodge</span></td>\r\n                            </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Canyon Express 16</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 7</span></td>\r\n                        <td class=\"lift-chair-icon chair3\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 8</span></td>\r\n                        <td class=\"lift-chair-icon chair3\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 21</span></td>\r\n                        <td class=\"lift-chair-icon chair3\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 22</span></td>\r\n                        <td class=\"lift-chair-icon chair3\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>High 5 Express</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Roller Coaster Express 4</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Schoolyard Express 17</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Village Gondola</span></td>\r\n                        <td class=\"lift-chair-icon gondola\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon closed\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 20</span></td>\r\n                        <td class=\"lift-chair-icon chair3\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                            <tr class=\"lift-header\">\r\n                                <td class=\"header-description\" colspan=\"4\"><span>Eagle Lodge</span></td>\r\n                            </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Chair 25</span></td>\r\n                        <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Cloud Nine Express 9</span></td>\r\n                        <td class=\"lift-chair-icon chair6\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                        <td class=\"lift-description\" colspan=\"1\"><span>Eagle Express 15</span></td>\r\n                        <td class=\"lift-chair-icon chair6\" colspan=\"1\"></td>\r\n                        <td class=\"lift-last-update\" colspan=\"1\"><span>2:26 PM</span></td>\r\n                    </tr>\r\n\r\n            </tbody>\r\n        </table>\r\n\r\n\r\n    </div>\r\n    <div class=\"col-md-12 col-sm-12\">\r\n\r\n        <h2>Legend</h2><table>\r\n                           <tbody>\r\n                               <tr class=\"lift-header\">\r\n                                   <td class=\"header-description\" colspan=\"4\"><span>Status</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-status-icon lift-open\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Open</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-status-icon sceniconly\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>For Scenic Rides Only</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-status-icon within30\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>30 Minutes or Less</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-status-icon expected\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Expected</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-status-icon weatherhold\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Hold - Weather</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-status-icon maintenancehold\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Hold - Maintenance</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-status-icon lift-closed\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Closed</span></td>\r\n                               </tr>\r\n                               <tr class=\"lift-header\">\r\n                                   <td class=\"header-description\" colspan=\"4\"><span>Type</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-chair-icon chair2\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Double Chair</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-chair-icon chair3\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Triple Chair</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-chair-icon chair4\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Quad Chair</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-chair-icon chair6\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Six-pack Chair</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-chair-icon gondola\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Gondola</span></td>\r\n                               </tr>\r\n                               <tr>\r\n                                   <td class=\"lift-chair-icon zipline\" colspan=\"1\"></td>\r\n                                   <td class=\"legend-description\" colspan=\"1\"><span>Zip Line</span></td>\r\n                               </tr>\r\n                           </tbody>\r\n        </table>\r\n    </div>\r\n</div>\r\n\r\n",
    'success': True,
    'Message': None
  }

  return JSONResponse(data)