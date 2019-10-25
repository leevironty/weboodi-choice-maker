import unittest
from weboodi.course import Option
from bs4 import BeautifulSoup as bs


class TestOption(unittest.TestCase):
    def test_normal(self):
        html = '''<tr>
    <td width="16%" valign="top" class="">
        <table width="100%" border="0">
            <tbody><tr>
                <th align="left" width="33%"><label for="ilmo2">Ilm.</label></th>
                <th align="left" width="33%"><label for="pois2">Peru</label></th>
                <th align="left" width="33%">Lkm </th>
            </tr>
            </tbody><tbody>
                <tr>

            <td width="33%" class="" valign="top"><input type="checkbox" id="ilmo2" name="OsaOpetTap0" value="1138052651"> </td>
            <td width="33%" class="" valign="top">&nbsp;</td>
            <td width="14%" align="right" valign="top" class="">

                36/36

            </td>




</tr>



<tr>
    <td colspan="3" class="">
        <font class="huom">  </font>
    </td>
</tr>


<tr>
    <td colspan="3" valign="top" class="">

    </td>
</tr>

<tr>
    <td colspan="3" align="left" class="">


        Ilmoittautumisaika


    </td>
</tr>
<tr>
    <td colspan="3" class="" align="left" valign="top" nowrap="">


        30.09.19
        klo 09.00-<br>
        04.11.19
        klo 23.59



    </td>
</tr>

</tbody>
</table>
</td>



<td class="" valign="top">
    <table width="100%" border="0" class="">
        <tbody>
            <tr>
                <td width="32%" valign="top" class="">
                    H01




                </td>
                <td width="32%" valign="top" class="">



                    <br>
                </td>
                <td width="36%" valign="top" class="">
                    <table width="100%" border="0" class="">
                        <tbody>
                            	<tr>
                                <td valign="top" class="" nowrap="">28.10.-02.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;ma&nbsp;14.15-16.00&nbsp;



<input type="HIDDEN" name="OpetPaikLink_5" value="1273">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_5" value="R001/U410b">

                                    <br>
                                    	</td></tr><tr>
                                <td valign="top" class="" nowrap="">31.10.-05.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;to&nbsp;14.15-16.00&nbsp;



<input type="HIDDEN" name="OpetPaikLink_6" value="12626">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_6" value="R001/Y229c">

                                    <br>

                            </td></tr>


                        </tbody></table>
                </td>
            </tr>


        </tbody>
    </table>








</td></tr>'''
        soup = bs(html, "lxml").body.tr
        opt = Option(soup, None)
        self.assertEqual(opt.name, "H01", "Name should be H01")
        self.assertTrue(opt.proposed, "Option should be proposed")
        self.assertEqual(len(opt.dates), 12, "Should happen 12 times")

    def test_not_normal(self):
        html = '''<tr>
    <td width="16%" valign="top" class="">
        <table width="100%" border="0">
            <tbody><tr>
                <th align="left" width="33%"><label for="ilmo7">Ilm.</label></th>
                <th align="left" width="33%"><label for="pois7">Peru</label></th>
                <th align="left" width="33%">Lkm </th>
            </tr>
            </tbody><tbody>
                <tr>
                    
            <td width="33%" class="" valign="top"><input type="checkbox" id="ilmo7" name="OsaOpetTap4" value="1140500618"> </td>
            <td width="33%" class="" valign="top">&nbsp;</td>
            <td width="14%" align="right" valign="top" class="">
                
                16/-
                
            </td>
            
            
            
            
</tr>




<tr>
    <td colspan="3" valign="top" class="">
        
    </td>
</tr>

<tr>
    <td colspan="3" align="left" class="">
        
        
        Ilmoittautumisaika
        
        
    </td>
</tr>
<tr>
    <td colspan="3" class="" align="left" valign="top" nowrap="">
        
        
        21.10.19
        klo 13.30-<br>
        04.11.19
        klo 23.59
        
        
        
    </td>
</tr>

</tbody>
</table>
</td>



<td class="" valign="top">
    <table width="100%" border="0" class="">
        <tbody>
            <tr>
                <td width="32%" valign="top" class="">
                    NA
                    

                    

                </td>
                <td width="32%" valign="top" class="">


                    
                    <br>
                </td>
                <td width="36%" valign="top" class="">
                    <table width="100%" border="0" class="">
                        <tbody>
                            <tr><td valign="top" class="">28.10.-05.12.19</td>

                                
                            </tr>


                        </tbody></table>
                </td>
            </tr>
            
            <tr>
                <td colspan="3" class=""><br></td>
            </tr>
            
            <tr>
                <td colspan="3" class=""><font color="#445a74">Ilmoittautumisen lisätiedot:</font>&nbsp;
                    
                    <p><span style="font-size:11pt;font-family:'calibri' , sans-serif">I have not registered for any of the exercise groups, but I wish to gain exercise points by returning homework.</span></p>&nbsp;</td>
            </tr>
            

        </tbody>
    </table>
    

    </td></tr>'''
        soup = bs(html, "lxml").body.tr
        opt = Option(soup, None)
        self.assertEqual(len(opt.dates), 0,  "Should not have events")

