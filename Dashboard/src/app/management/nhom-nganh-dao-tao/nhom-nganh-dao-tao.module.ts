import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { ImageCroppingComponent } from '@component-shared/image-cropping/image-cropping.component';
import { UploadFileComponent } from '@component-shared/upload-file/upload-file.component';
import { ViewFileComponent } from '@component-shared/view-file/view-file.component';
import { BreadcrumbComponent } from '@widget/breadcrumb/breadcumb.component';
import { FieldErrorDisplayComponent } from '@widget/field-error-display/field-error-display.component';
import { TablePaginateComponent } from '@widget/paginate/paginate.component';
import { BlobToB64Pipe } from '@widget/pipes/blob-to-base64.pipe';
import { ImgIdToBlobPipe } from '@widget/pipes/img-id-to-blob.pipe';
import { NzButtonModule } from 'ng-zorro-antd/button';
import { NzGridModule } from 'ng-zorro-antd/grid';
import { NzInputModule } from 'ng-zorro-antd/input';
import { NzModalModule } from 'ng-zorro-antd/modal';
import { NzSwitchModule } from 'ng-zorro-antd/switch';
import { NzTableModule } from 'ng-zorro-antd/table';
import { FormNhomNganhDaoTaoComponent } from './form-nhom-nganh-dao-tao/form-nhom-nganh-dao-tao.component';
import { ListNhomNganhDaoTaoComponent } from './list-nhom-nganh-dao-tao/list-nhom-nganh-dao-tao.component';


export const pluginsModules = [
  NzGridModule,
  NzTableModule,
  NzInputModule,
  NzButtonModule,
  NzModalModule,
  NzSwitchModule,
  FieldErrorDisplayComponent,
  TablePaginateComponent,
  BreadcrumbComponent,
  ImageCroppingComponent,
  BlobToB64Pipe,
  ImgIdToBlobPipe,
  UploadFileComponent,
  ViewFileComponent,
];

export const routes: Routes = [
  { path: '', component: ListNhomNganhDaoTaoComponent },
];

@NgModule({
  declarations: [
    // Component here
    ListNhomNganhDaoTaoComponent,
    FormNhomNganhDaoTaoComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    pluginsModules,

    // Routes
    RouterModule.forChild(routes),
  ],
})
export class NhomNganhDaoTaoModule { }
