import unittest
from weboodi.course import Category
from bs4 import BeautifulSoup as bs


class TestCategory(unittest.TestCase):
    def test_normal(self):
        html = '''<table border="0" width="100%" class="kll"> 
    <tbody><tr valign="bottom">
        <td width="16%" class="ILMO">
            <table width="100%" border="0">
                <tbody>
                    <tr><th align="left" class="tyyppi" colspan="3"><table border="0" width="100%">
                    <tbody><tr valign="bottom">
                        <th align="left" colspan="3">Ilmoittautuminen</th>
                    </tr></tbody></table>
    </th></tr>
    </tbody>
</table>
</td>

<th>
<table width="100%" border="0">
    <tbody>
        <tr>
            <th><table width="100%" border="0">
        <tbody>
            <tr>
                <th align="left" class="tyyppi" colspan="3">
                    
                    
                </th>
            </tr>
            <tr>
                
                <th width="32%" align="left" valign="bottom">
                    
                    Harjoitukset&nbsp;
                    
                </th>
                <th width="32%" align="left" valign="bottom">
                    Opettaja
                </th>
                <th width="36%" align="left" valign="bottom">
                     <br>Aika ja Paikka 
                </th>
            </tr>
        </tbody>
    </table>
    </th>
    </tr>
    </tbody>
</table>
</th>
</tr>



<tr>
    <td width="16%" valign="top" class="">
        <table width="100%" border="0">
            <tbody><tr>
                <th align="left" width="33%"><label for="ilmo2">Ilm.</label></th>
                <th align="left" width="33%"><label for="pois2">Peru</label></th>
                <th align="left" width="33%">Lkm </th>
            </tr>
            </tbody><tbody>
                <tr>
                    
            <td colspan="3" class=""><table width="100%"><tbody><tr>
                        <td colspan="2" class="">&nbsp;</td>
                        <td width="14%" align="right" valign="top" class="">
                            
                            36/36
                            
                        </td>
                    </tr>
                </tbody></table>
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
    







</td></tr><tr>
    <td width="16%" valign="top" class="">
        <table width="100%" border="0">
            <tbody><tr>
                <th align="left" width="33%"><label for="ilmo3">Ilm.</label></th>
                <th align="left" width="33%"><label for="pois3">Peru</label></th>
                <th align="left" width="33%">Lkm </th>
            </tr>
            </tbody><tbody>
                <tr>
                    
            <td colspan="3" class=""><table width="100%"><tbody><tr>
                        <td colspan="2" class="">&nbsp;</td>
                        <td width="14%" align="right" valign="top" class="">
                            
                            36/36
                            
                        </td>
                    </tr>
                </tbody></table>
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
                    H02
                    

                    

                </td>
                <td width="32%" valign="top" class="">


                    
                    <br>
                </td>
                <td width="36%" valign="top" class="">
                    <table width="100%" border="0" class="">
                        <tbody>
                            	<tr> 
                                <td valign="top" class="" nowrap="">29.10.-03.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;ti&nbsp;14.15-16.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_7" value="1133297619">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_7" value="R001/Majakka">

                                    <br>
                                    	</td></tr><tr> 
                                <td valign="top" class="" nowrap="">01.11.-29.11.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;pe&nbsp;14.15-16.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_8" value="12655">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_8" value="R001/Y228b">

                                    <br>
                                    	</td></tr><tr> 
                                <td valign="top" class="" nowrap="">05.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;to&nbsp;14.15-16.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_9" value="1280">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_9" value="R001/Y228a">

                                    <br>
                                    
                            </td></tr>


                        </tbody></table>
                </td>
            </tr>
            

        </tbody>
    </table>
    







</td></tr><tr>
    <td width="16%" valign="top" class="">
        <table width="100%" border="0">
            <tbody><tr>
                <th align="left" width="33%"><label for="ilmo4">Ilm.</label></th>
                <th align="left" width="33%"><label for="pois4">Peru</label></th>
                <th align="left" width="33%">Lkm </th>
            </tr>
            </tbody><tbody>
                <tr>
                    
            <td colspan="3" class=""><table width="100%"><tbody><tr>
                        <td colspan="2" class="">&nbsp;</td>
                        <td width="14%" align="right" valign="top" class="">
                            
                            36/36
                            
                        </td>
                    </tr>
                </tbody></table>
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
                    H03
                    

                    

                </td>
                <td width="32%" valign="top" class="">


                    
                    <br>
                </td>
                <td width="36%" valign="top" class="">
                    <table width="100%" border="0" class="">
                        <tbody>
                            	<tr> 
                                <td valign="top" class="" nowrap="">29.10.-03.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;ti&nbsp;12.15-14.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_10" value="12626">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_10" value="R001/Y229c">

                                    <br>
                                    	</td></tr><tr> 
                                <td valign="top" class="" nowrap="">31.10.-05.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;to&nbsp;10.15-12.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_11" value="12655">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_11" value="R001/Y228b">

                                    <br>
                                    
                            </td></tr>


                        </tbody></table>
                </td>
            </tr>
            

        </tbody>
    </table>
    







</td></tr><tr>
    <td width="16%" valign="top" class="">
        <table width="100%" border="0">
            <tbody><tr>
                <th align="left" width="33%"><label for="ilmo5">Ilm.</label></th>
                <th align="left" width="33%"><label for="pois5">Peru</label></th>
                <th align="left" width="33%">Lkm </th>
            </tr>
            </tbody><tbody>
                <tr>
                    
            <td colspan="3" class=""><table width="100%"><tbody><tr>
                        <td colspan="2" class="">&nbsp;</td>
                        <td width="14%" align="right" valign="top" class="">
                            
                            36/36
                            
                        </td>
                    </tr>
                </tbody></table>
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
                    H04
                    

                    

                </td>
                <td width="32%" valign="top" class="">


                    
                    <br>
                </td>
                <td width="36%" valign="top" class="">
                    <table width="100%" border="0" class="">
                        <tbody>
                            	<tr> 
                                <td valign="top" class="" nowrap="">30.10.-04.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;ke&nbsp;08.15-10.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_12" value="12626">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_12" value="R001/Y229c">

                                    <br>
                                    	</td></tr><tr> 
                                <td valign="top" class="" nowrap="">01.11.-29.11.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;pe&nbsp;08.15-10.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_13" value="12627">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_13" value="R001/Y229a">

                                    <br>
                                    	</td></tr><tr> 
                                <td valign="top" class="" nowrap="">05.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;to&nbsp;08.15-10.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_14" value="12627">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_14" value="R001/Y229a">

                                    <br>
                                    
                            </td></tr>


                        </tbody></table>
                </td>
            </tr>
            

        </tbody>
    </table>
    







</td></tr><tr>
    <td width="16%" valign="top" class="">
        <table width="100%" border="0">
            <tbody><tr>
                <th align="left" width="33%"><label for="ilmo6">Ilm.</label></th>
                <th align="left" width="33%"><label for="pois6">Peru</label></th>
                <th align="left" width="33%">Lkm </th>
            </tr>
            </tbody><tbody>
                <tr>
                    
            <td colspan="3" class=""><table width="100%"><tbody><tr>
                        <td colspan="2" class="">&nbsp;</td>
                        <td width="14%" align="right" valign="top" class="">
                            
                            36/36
                            
                        </td>
                    </tr>
                </tbody></table>
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
                    H05
                    

                    

                </td>
                <td width="32%" valign="top" class="">


                    
                    <br>
                </td>
                <td width="36%" valign="top" class="">
                    <table width="100%" border="0" class="">
                        <tbody>
                            	<tr> 
                                <td valign="top" class="" nowrap="">29.10.-26.11.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;ti&nbsp;16.15-18.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_15" value="12626">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_15" value="R001/Y229c">

                                    <br>
                                    	</td></tr><tr> 
                                <td valign="top" class="" nowrap="">01.11.-29.11.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;pe&nbsp;16.15-18.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_16" value="12627">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_16" value="R001/Y229a">

                                    <br>
                                    	</td></tr><tr> 
                                <td valign="top" class="" nowrap="">03.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;ti&nbsp;16.15-18.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_17" value="12627">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_17" value="R001/Y229a">

                                    <br>
                                    	</td></tr><tr> 
                                <td valign="top" class="" nowrap="">05.12.19
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;to&nbsp;16.15-18.00&nbsp;
                                    


<input type="HIDDEN" name="OpetPaikLink_18" value="1271">
<input type="SUBMIT" class="submit2" name="LINKOPETPAIK_18" value="R001/U406a">

                                    <br>
                                    
                            </td></tr>


                        </tbody></table>
                </td>
            </tr>
            

        </tbody>
    </table>
    







</td></tr><tr>
    <td width="16%" valign="top" class="">
        <table width="100%" border="0">
            <tbody><tr>
                <th align="left" width="33%"><label for="ilmo7">Ilm.</label></th>
                <th align="left" width="33%"><label for="pois7">Peru</label></th>
                <th align="left" width="33%">Lkm </th>
            </tr>
            </tbody><tbody>
                <tr>
                    
            <td colspan="3" class=""><table width="100%"><tbody><tr>
                        <td colspan="2" class="">&nbsp;</td>
                        <td width="14%" align="right" valign="top" class="">
                            
                            19/-
                            
                        </td>
                    </tr>
                </tbody></table>
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
    

    </td></tr></tbody></table>'''
        soup = bs(html, "lxml").body.table
        cat = Category(soup, None)
        self.assertEqual(cat.name, "Harjoitukset", "Name should be Harjoitukset")
        self.assertEqual(len(cat.options), 6, "Should have 6 options")
        self.assertEqual(len(cat.proposed ), 6, "Should have 6 proposd options")
        self.assertFalse(cat.is_ready, "Should not be ready")


